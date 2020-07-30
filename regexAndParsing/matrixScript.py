#!/bin/python3
import re


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    encoded_string = "".join([matrix[j][i] for i in range(m) for j in range(n)])
    pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
    print(re.sub(pat, ' ', encoded_string))
