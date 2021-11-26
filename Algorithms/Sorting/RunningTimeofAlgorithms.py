#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    shift=0
    for n in range(1, len(arr)):
        val = arr[n]
        last=-1
        #while (last <= n-1):
        for last in range(n-1, -1, -1):
            if arr[last] > val:
                arr[last+1] = arr[last]
                shift +=1
            else:
                arr[last+1] = val
                break
            last -=1
        if arr[0] > val:
            arr[0] = val
    return shift

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
