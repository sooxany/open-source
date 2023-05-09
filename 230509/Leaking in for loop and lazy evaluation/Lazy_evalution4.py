list_fun_curry = [(lambda  x: (lambda: x))(i) for i in range(10)]

for f in list_fun_curry:
    print(f())