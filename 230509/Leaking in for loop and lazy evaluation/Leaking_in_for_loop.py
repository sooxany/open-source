i = 20

list_a = []
for i in range(10):
    list_a.append(2*i)

print(i) # print 9 --leaking--

i = 20

list_b = [2*i for i in range(10)]

print(i) # print 20 --no leaking--