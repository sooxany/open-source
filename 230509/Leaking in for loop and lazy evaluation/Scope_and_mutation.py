def print_12():
    x=[1,2]
    print(x)

def print_x_outside():
    x[0] = 3
    print(x)

x = ['a','b']

def main():
    def print_x_inside():
        x[1] = 'b'
        print(x)

    x = [1,2]
    print_x_inside() # [1,b]
    print(x) # [1,b]
    print_12() # [1,2]

    x=[1,2,3]
    print_x_outside() # [3,b]
    print_x_inside() # [1,b,3]
    print(x) # [1,b,3]
    print_12() #[1,2]

main()
print(x)