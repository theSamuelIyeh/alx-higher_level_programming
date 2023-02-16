#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    len1 = len(matrix)
    for list1 in range(0, len1):
        len2 = len(matrix[list1])
        for list2 in range(0, len2):
            print("{}".format(matrix[list1][list2]), end=" ")
        print("\n")
