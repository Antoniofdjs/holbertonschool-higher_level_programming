#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = list.copy(my_list)
    for i in range(0, len(my_list)):
        if int(my_list[i]) % 2 == 0:
            list_result[i] = True
        else:
            list_result[i] = False
    return list_result
