list_fun = []
for i in range(10):
    list_fun.append(lambda: i)

for f in list_fun:
    print(f())

print(i) # print 9 ten times --> lambda 때문에

