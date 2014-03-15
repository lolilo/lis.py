var s =
    {
         "define": [
              "define",
              "area",
              [
                   "lambda",
                   [
                        "r"
                   ],
                   [
                        "*",
                        3.141592653,
                        [
                             "*",
                             "r",
                             "r"
                        ]
                   ]
              ]
         ]
    };


var BinaryTreeNode = function (value) {
  this.value = value;
  this.left = null;
  this.right = null;

  this.get_left = function () {
    return this.left;
  };

  this.get_right = function () {
    return this.right;
  };

  this.set_left = function (node) {
    this.left = node;
  };

  this.set_right = function (node) {
    this.right = node;
  };

  this.get_value = function () {
    return this.value;
  };
};

test_initial = function(s){

  for (var key in s){

    // (define var exp)
    if (key=="define"){

      define_list = s[key];
      var variable = define_list[1];
      var exp = define_list[2];

      console.log(key);
      console.log(variable);

      test(exp);
      // for (var i in s_list){
      //   console.log(s_list[i]);
      // }
    }
  }
};

test = function(list){
  
  var parent = new BinaryTreeNode(list[0]);
  // console.log(first);
  if (parent.value=="lambda"){
    var lamda = parent.value;
    var variable = new BinaryTreeNode(list[1][0]);
    var exp = new BinaryTreeNode(list[2]);
    // var exp_symbol = exp.value[0];
    

    parent.set_left(variable);
    parent.set_right(exp);
    console.log(parent);

    // FIX THIS. instead of exp_symbol, test(exp) should be the second arg
    // console.log(variable, "     ", test(exp));


    // console.log("YOOOO");
    // oh...test(exp) evaluates before this entire line is printed. gotta return stuff, not print
    // well, this is more complicated than what I began with
    // console.log(variable, "     ", test(exp));
    // test(exp);
  }
  // modify later for if first in global_env or env
  else if (parent.value=="*"){
    // console.log(list);

    console.log();
    console.log('making children with this list', list);
    var eval_child1 = test(list[1]);
    console.log('inbetween');
    var eval_child2 = test(list[2]);
    console.log('the children are', eval_child1, eval_child2);

    var child1 = new BinaryTreeNode(list[1]);
    var child2 = new BinaryTreeNode(list[2]);

    parent.set_left(child1);
    parent.set_right(child2);
    // console.log(parent);
    return parent;
  }

  else {
    return list;
  }




                   // [
                   //      "*",
                   //      3.141592653,
                   //      [
                   //           "*",
                   //           "r",
                   //           "r"
                   //      ]





};

test_initial(s);

// console.log(Object.keys(s));

