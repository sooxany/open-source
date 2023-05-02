import pickle

pickle.dumps(fibonacci)

# functools.wraps copies all of the important metadata about the inner function 
# to the outer function
from functools import wraps

def trace(func):
    @wraps(func)
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
help(fibonacci)
import pickle
print(pickle.dumps(fibonacci))
print(fibonacci(4))