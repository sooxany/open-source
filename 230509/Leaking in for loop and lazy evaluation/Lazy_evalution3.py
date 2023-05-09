list_fun_hack = [lambda i=i: i for i in range(10)]

for f in list_fun_hack:
    print(f())