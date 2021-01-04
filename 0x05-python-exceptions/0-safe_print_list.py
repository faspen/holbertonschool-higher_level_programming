def safe_print_list(my_list=[], x=0):
    i = 0
    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            num += 1
        except IndexError:
            print("")
            return num
    print("")
    return num
