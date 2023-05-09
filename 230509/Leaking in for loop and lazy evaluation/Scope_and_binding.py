def main():
    def print_modify(new_value):
        nonlocal x # 이게 있어야 함
        print(x)
        x = new_value

    x=10
    print_modify(11)

main()