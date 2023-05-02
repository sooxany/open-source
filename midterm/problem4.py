def drive():
    x = list(range(3))

    y = x.copy()
    y.append(5)

    x = sum(y[:3])
    print(x)

    x = sum(y[2:-1])
    print(x)

    x = sum(y[3:])
    print(x)

if __name__== "__main__":
    drive()


# answer

def drive():
    x = list(range(3))

    y = x.copy()
    y.append(5)

    def sum_range(lst, start, end):
        return sum(lst[start:end])

    x = sum_range(y, 0, 3)
    print(x)

    x = sum_range(y, 2, -1)
    print(x)

    x = sum_range(y, 3, len(y))
    print(x)

if __name__ == "__main__":
    drive()
