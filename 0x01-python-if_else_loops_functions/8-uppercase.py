#!/usr/bin/python3
def uppercase(str):
    newString = ""
    for i in str:
        char = ord(i)
        if 97 <= char <= 122:
            diff = char - 97
            newChar = diff + 65
            newString = newString + chr(newChar)
        else:
            newString = newString + i
    print("{0}".format(newString))
