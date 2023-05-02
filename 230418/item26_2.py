def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
 """Return the n-th Fibonacci number"""
 if n in (0, 1):
    return n;
 return (fibonacci(n - 2) + fibonacci(n - 1))

# Way 1
print('- Way 1 -')
print(fibonacci(4))

# Way 2
fibonacci = trace(fibonacci)
print('- Way 2 -')
print(fibonacci(4))
print(help(fibonacci)) 