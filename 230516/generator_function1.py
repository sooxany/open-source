def letter_by_list(a,z):
    rst = []
    while ord(a) < ord(z):
        rst.append(a)
        a = chr(ord(a)+1)
    return rst

def letter_by_generator(a,z):
    while ord(a) < ord(z):
        yield a
        a = chr(ord(a)+1)

if __name__ == "__main__":
    print(letter_by_list('m','v'))
    print(list(letter_by_generator('m','v')))