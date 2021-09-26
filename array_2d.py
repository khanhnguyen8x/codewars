#!/bin/python3

import math
import os
import random
import re
import sys

def print_matrix(arr):
    for m in range(6):
        row = list()
        for n in range(6):
            row.append(str(arr[m][n]))
        print(" ".join(row))

def sum_matrix(arr, i, j):
    m = 6
    n = 6
    max_m = 4
    max_n = 4
    sum_matrix = 0
    if i < max_m and j < max_n:
        sum_matrix = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
    return sum_matrix


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = sum_matrix(arr, 0, 0)
    for i in range(4):
        for j in range(4):
            result = max(result, sum_matrix(arr, i, j))
    print(result)
