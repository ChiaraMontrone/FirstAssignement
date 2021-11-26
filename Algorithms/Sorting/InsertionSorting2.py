#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    val = arr[n]
    last=-1
    for last in range(n-1, -1, -1):
        if arr[last] > val:
            arr[last+1] = arr[last]
        else:
            arr[last+1] = val
            break
        last -=1
    if arr[0] > val:
        arr[0] = val

def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        insertionSort1(i, arr)
        print(" ".join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
