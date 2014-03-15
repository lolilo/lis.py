var define =
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

var s =
                    {
                         "*": [
                              "*",
                              9,
                              8
                         ]
                    };



var BinaryTreeNode = function (value) {
  this.value = value;
  this.left = null;
  this.right = null;

  this.getLeft = function () {
    return this.left;
  };

  this.getRight = function () {
    return this.right;
  };

  this.setLeft = function (node) {
    this.left = node;
  };

  this.setRight = function (node) {
    this.right = node;
  };

  this.getValue = function () {
    return this.value;
  };
};

// after we set the tree up, traverse the tree to "draw" it on the frontend
var depthFirstTraversal = function (node) {
  if (node === null) {
    return;
  }
  
  // need to store nodes as a list and return at the end?
  // well, we could generate images as we are traversing...

  console.log(node.value);
  depthFirstTraversal(node.getLeft());
  depthFirstTraversal(node.getRight());
  // console.log('this is returning!');
  // console.log(node.getValue());
  // return node.getValue();
};



test_initial = function(s){

  for (var key in s){
    // console.log(key);
    // first and only -- each object has only one key
    dict_entry = s[key];
    // console.log(dict_entry);
    tree = test(dict_entry);
    
    console.log('this is the final tree');
    console.log(tree);
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

    if (parent.value=="define"){
      var define = parent.value;
      var define_variable = new BinaryTreeNode(list[1]);

      var define_exp = list[2];

      parent.setLeft(define_variable);
      parent.left.setLeft(test(define_exp));

    }

    else if (parent.value=="lambda"){
      var lamda = parent.value;
      var lambda_variable = new BinaryTreeNode(list[1][0]);

      // right now, value is an object
      // var exp = new BinaryTreeNode(list[2]);

      var lambda_exp = list[2];

      parent.setLeft(lambda_variable);
      parent.setRight(test(lambda_exp));

      // console.log(parent);
      // console.log(depthFirstTraversal(parent));
    }
    // modify later for if first in global_env or env
    else if (parent.value=="*"){
  
      console.log();
      var child1 = test(list[1]);
      var child2 = test(list[2]);
      // console.log('the children are', eval_child1, eval_child2);
  
      parent.setLeft(child1);
      parent.setRight(child2);
      // console.log('values!', parent.left.value, parent.right.value);
      // console.log(parent);
      return parent;
    }
    // console.log();
    // console.log('this is the final tree');
    return parent;
  }


};

test_initial(define);


