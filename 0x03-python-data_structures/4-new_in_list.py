#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        temp_list[idx] = element
        return temp_list
