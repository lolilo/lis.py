s = """
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
    }, 
"""

print s.replace(":", ' ').replace('{', ' ').replace('[', ' ').replace('}', ' ').replace(']', ' ')

