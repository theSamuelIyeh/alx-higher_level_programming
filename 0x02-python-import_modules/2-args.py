#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv)
    start = 1
    if number <= 1:
        print("0 arguments.")
    elif number == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(number - 1))
    while start < number:
        print("{}: {}".format(start, argv[start]))
        start += 1
