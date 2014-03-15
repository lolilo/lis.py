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

// console.log(s);
// console.log(typeof(s));


// takes in a list and returns the variable being defined
// var_being_defined = function(ls){
//   return ls[1];
// };


test = function(s){

  for (var key in s){

    // (define var exp)
    if (key=="define"){

      define_list = s[key];
      var variable = define_list[1];
      var exp = define_list[2];

      console.log(exp);
      // for (var i in s_list){
      //   console.log(s_list[i]);
      // }
    }
  }
};

test(s);

// console.log(Object.keys(s));

