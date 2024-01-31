#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
# better to do a loop for all individual divisions and catch errors this way
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
# The 'excepts' below will catch errors that pop from 'try' and do the block
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
# finally will be done regardless of what 'except' and 'try' do
        finally:
            pass

    return new_list
