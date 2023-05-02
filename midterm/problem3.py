# 스택 머신의 이해

def print_m():
    x = 100
    print(x)

def print_outside():
    print(x)

x = 10

def main():
    def print_inside():
        print(x)

    x = 9
    print_m() # 100
    print_inside() # 9

    x = 18 # main의 local value가 바뀐 것이다
    print_outside() # 10
    print_m() # 100
    print_inside() # 18

if __name__ == "__main__":
    main()
