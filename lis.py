# Scheme interpreter written in Python
""" program --> Parser --> representation --> Execution --> output """

"""          Symbol, Env classes           """

class Env(dict):
    # Env is a subclass of dict.
    # An environment is a dictionary of {'var': val} pairs with an outer Env.
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        # Find the innermost Env where var appears.
        # Env.find finds the right environment according to lexical scoping rules.


        # return self if var in self else self.outer.find(var)
        # weird syntax?
        if var in self:
            return self
        else: 
            self.outer.find(var)
            # Return the lowest index in the string where substring sub is found, 
            # such that sub is contained in the slice s[start:end]...a string? Huh?

def add_globals(env):
    # Add Scheme standard procedures to an environment.
    import math, operator as op
    env.update(vars(math)) # vars(object) is equivalent to object.__dict__
    env.update({
            '+' : op.add, 
            '-' : op.sub, 
            '*' : op.mul, 
            '/' : op.div, 
            'not' : op.not_,
            '>' : op.gt,
            '<' : op.lt,
            '>=' : op.ge,
            '<=' : op.le,
            '=' : op.eq,
            'equal?' : op.eq, # values are equal
            'eq?' : op.is_, # point to the same object in memory
            'length' : len,

            # Lambda forms (lambda expressions) have the same syntactic position as
            # expressions.  They are a shorthand to create anonymous functions; the
            # expression ``lambda arguments: expression`` yields a function object.

            'cons' : lambda x, y : [x] + y, # what the shit is this
            'car' : lambda x : x[0],
            'cdr' : lambda x : x[1:],
            'append' : op.add, # this works for Scheme, I guess? 
            'list' : lambda *x : list(x),
            # list() -> new empty list
            # list(iterable) -> new list initialized from iterable's items
            # syntactic sugar. l = [] is the same as l = list()
            'list?' : lambda x : isa(x, list),
            'null?' : lambda x : x == [],
            'symbol?' : lambda x : isa(x, Symbol)    
        })
    return env

global_env = add_globals(Env())


"""          eval           """

# Evaluate an expression x in an environment env.
def eval(x, env=global_env):
    print 'env!', env
    print """



    """
    print global_env
    
    # variable reference
    if isa(x, Symbol):
        return env.find(x)[x]
        # env.find is the same as env.__getitem__
    
    # constant literal
    elif not isa(x, list):
        return x

    # (quote exp)
    elif x[0] == 'quote':
        (_, exp) = x # _ is a character we use as a variable.
        return exp

    # conditional (if test conseq alt)
    elif x[0] == 'if':
        (_, test, conseq, alt) = x

    # assignment (set! var exp)
    elif x[0] == 'set!':
        (_, var, exp) = x
        env.find(var)[var] = eval(exp, env) # recursively eval the expression

    # (define var exp)
    elif x[0] == 'define':
        (_, var, exp) = x
        env[var] = eval(exp, env) # adds var to the global environment dictionary

    # procedure (lambda (var*) exp)
    elif x[0] == 'lambda':
        (_, vars, exp) = x
        return lambda *args: eval(exp, Env(vars, args, env))

    # sequencing (being exp*)
    elif x[0] == 'begin':
        for exp in x[1:]:
            val = eval(exp, env)
        return val # val will keep being reassigned, so we only return the last val?

    else:
        # procedure call (proc exp*)
        exps = [eval(exp, env) for exp in x] # list of evaluated exp
        proc = exps.pop(0) # Are we arbitrarily choosing the first element of the exps list?
        # Nope. Recursive call of sorts...solidify this later.
        return proc(*exps) # arbitrary amount of exps, which will be recursively evaluated

# alias
isa = isinstance # isinstance(9, int) --> True, isinstance(9, str) --> False
Symbol = str

"""          parse, read, user interaction           """

# Parsing is traditionally separated into two parts: lexical analysis, 
# in which the input character string is broken up into a sequence of tokens, 
# and syntactic analysis, in which the tokens are assembled into an internal representation. 
# The Lispy tokens are parentheses, symbols (such as set! or x), and numbers (such as 2).

def read(s):
    # read a Scheme expression from a string
    return read_from(tokenize(s))

parse = read # Why? Why not def parse(s)?

def tokenize(s):
    # convert a string into a list of tokens
    # add white space in between parentheses and split on white space
    return s.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from(tokens):
    # read an expression from a sequence of tokens
    if len(tokens) == 0:
        raise SyntaxError('unexpect EOF while reading')
    token = tokens.pop(0)

    if '(' == token:
        l = []
        while tokens[0] != ')':
            l.append(read_from(tokens))
        tokens.pop(0) # pop off ')'
        return l

    # account for '()'
    elif ')' == token:
        raise SyntaxError('unexpected token )')

    else:
        return atom(token)

def atom(token):
    # numbers become numbers
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)

        # every other token is a symbol
        except ValueError:
            return Symbol(token)

def to_string(exp):
    # convert Python object back into Lisp-readable string
    if isa(exp, list):
        return '(' + ' '.join(map(to_string, exp)) + ')'
    else:
        str(exp) # called via the map function above. fancy.
        # can simply write .join(map(str(exp), exp)) above? 

def repl():

    print global_env
    # prompt-read-eval-print loop
    while True:
        # able to push enter infinitely
        user_input = raw_input('lis.py > ')
        if user_input:
            val = eval(parse(user_input))
            if val is not None:
            # if val:
                print to_string(val)

# print global_env
