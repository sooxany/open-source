a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

alt = map(lambda x: x**2, a)
print(list(alt)) # for output, but too noisy!