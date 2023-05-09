def fun3():
    my_list = [1,2,3]
    for value in my_list:
        value += 5
    print(my_list)

fun3()

def fun4():
    my_list = [1,2,3]
    for i in range(len(my_list)):
        my_list[i] += 5
    print(my_list)

fun4()