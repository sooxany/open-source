
# binding 때문에 변경이 안됨
def func9():
    x = [1,2,3]
    add_five(x)
    print(x)

def add_five(x):
    x = [1,2,3,5]

func9()
