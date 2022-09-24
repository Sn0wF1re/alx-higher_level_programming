#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        copyList = my_list.copy()
        copyList[idx] = element
        return (copyList)
    else:
        return (my_list)
