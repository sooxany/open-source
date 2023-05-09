def fun8():
    x = [1,2,3]
    add_five(x)
    print(x)

def add_five(some_list):
    some_list.append(5) # call-by-refenence

fun8()