#피보나치
from inspect import trace


def frace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper()

@trace
def fibonacci(n):
    if n in (0,1):
        return n;
    return (fibonacci(n-2)+fibonacci(n-1))

if __name__ == "__main__":
    print(fibonacci(0))