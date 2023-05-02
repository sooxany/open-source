a = [-1, 0, 1, 2, 3]

alt = map(lambda x: x**2, filter(lambda x: x%2==0, a))
print(list(alt))

#answer

a = [-1, 0, 1, 2, 3]

alt = [x**2 for x in a if x % 2 == 0]
print(alt)
