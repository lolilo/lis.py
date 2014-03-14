l = [9,9,9,9,9]

del l[0]
print l

user@chromebox-003:~/src/project$ time python del.py 
[9, 9, 9, 9]

real    0m0.040s
user    0m0.031s
sys 0m0.007s
user@chromebox-003:~/src/project$ time python pop.py
[9, 9, 9, 9]

real    0m0.032s
user    0m0.026s
sys 0m0.006s
user@chromebox-003:~/src/project$ time python del.py 
[9, 9, 9, 9]

real    0m0.036s
user    0m0.031s
sys 0m0.004s
user@chromebox-003:~/src/project$ time python pop.py
[9, 9, 9, 9]

real    0m0.027s
user    0m0.020s
sys 0m0.007s
user@chromebox-003:~/src/project$ time python pop.py
[9, 9, 9, 9]

real    0m0.031s
user    0m0.020s
sys 0m0.011s
user@chromebox-003:~/src/project$ time python del.py 
[9, 9, 9, 9]

real    0m0.035s
user    0m0.028s
sys 0m0.005s
