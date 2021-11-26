#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    pivot = arr[0]
    left = []
    right = []
    final = []
    equal = []
    for value in arr:
        if value < pivot:
            left.append(value)
        if value > pivot:
            right.append(value)
        
    equal = []
    equal.append(pivot)
    final =  left + equal + right

    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
