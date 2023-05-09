def fun_gen(n):
    i = 0
    while i < n:
        yield (lambda: i)
        i += 1

for f in fun_gen(10):
    print(f()) # print 0 1 2 3 4 5 6 7 8 9

for f in list(fun_gen(10)):
    print(f()) # print 10이 10번