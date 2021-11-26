#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    val = arr[-1]
    last = n - 2
    while (val <= arr[last]) and (last >= 0):
        arr[last+1] = arr[last]
        print(' '.join(str(x) for x in arr))

        last -= 1
    arr[last+1] = val
    print(' '.join(str(x) for x in arr))

        
            
            
        
        
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
