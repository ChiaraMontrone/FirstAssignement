#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum_min = int(0) 
    sum_max = int(0)
    arr.sort()

    a = arr.pop(4)
    for element in arr:
        sum_min += element
    arr.append(a)
    arr.pop(0)
    for element in arr:
        sum_max += element
    
    print(sum_min,sum_max)
            
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
