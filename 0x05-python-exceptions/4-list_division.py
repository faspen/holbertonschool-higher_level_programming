#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    math = 0
    for i in range(list_length):
        try:
            math = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            div_list.append(math)
        math = 0
    return div_list
