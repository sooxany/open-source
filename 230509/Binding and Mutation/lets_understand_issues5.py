def fun7():
    x = 0
    add_five(x)
    print(x)

def add_five(x):
    x += 5 # call-by-value

fun7()