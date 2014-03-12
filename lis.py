# Scheme interpreter written in Python
""" program --> Parser --> representation --> Execution --> output """

"""          Symbol, Env classes           """

class Env(dict):
    # Env is a subclass of dict.
    # An environment is a dictionary of {'var': val} pairs with an outer Env.
    def __init__(self, parms=(), outer=None):
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

    def add_global(env):
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
    
    # variable reference
    if isa(x, Symbol):
        return env.find(x)[x]
    
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


isa = isinstance # isinstance(9, int) --> True, isinstance(9, str) --> False
Symbol = str



"""          parse, read, user interaction           """

