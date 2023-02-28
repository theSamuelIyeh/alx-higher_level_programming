#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        num = 0
        try:
            num = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            num = 0
        except ZeroDivisionError:
            print("division by 0")
            num = 0
        except IndexError:
            print("out of range")
            num = 0
        finally:
            new_list.append(num)
            continue
    return new_list
