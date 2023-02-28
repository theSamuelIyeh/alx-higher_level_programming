#!/usr/bin/python3
if __name__ == "__main__":
    def safe_print_list(my_list=[], x=0):
        try:
            count = 0
            for i in range(0, x):
                print("{:d}".format(my_list[i]), end='')
                count += 1
            print()
        except IndexError:
            return count
