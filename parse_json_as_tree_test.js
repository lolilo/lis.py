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

  // single value string or int or etc.
  if (typeof(list) != typeof([])){
    // console.log(list);
    return new BinaryTreeNode(list);
  }

  else {
    var parent = new BinaryTreeNode(list[0]);

    if (parent.value=="lambda"){
      var lamda = parent.value;
      var variable = new BinaryTreeNode(list[1][0]);

      // right now, value is an object
      // var exp = new BinaryTreeNode(list[2]);

      exp = list[2];

      parent.set_left(variable);
      parent.set_right(test(exp));

      // console.log(exp.left.value, exp.right.value);
      console.log(parent);
    }
    // modify later for if first in global_env or env
    else if (parent.value=="*"){
  
      console.log();
      var child1 = test(list[1]);
      var child2 = test(list[2]);
      // console.log('the children are', eval_child1, eval_child2);
  
      parent.set_left(child1);
      parent.set_right(child2);
      // console.log('values!', parent.left.value, parent.right.value);
      // console.log(parent);
      return parent;
    }
  }
};

test_initial(s);


