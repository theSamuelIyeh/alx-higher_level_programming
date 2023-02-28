#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end='')
            count += 1
        return count
    except (ValueError, TypeError):
        pass
    except IndexError:
        print()
        return count
