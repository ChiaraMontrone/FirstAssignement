#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negative = 0
    positive = 0
    counter = 0
    for i in arr:
        if i < 0:
            negative = negative + 1
        
        elif i > 0:
            positive = positive + 1
            
        else:
            counter = counter + 1
            
    print("{:.6f}".format(round(positive/len(arr),6)))
    print("{:.6f}".format(round(negative/len(arr),6)))
    print("{:.6f}".format(round(counter/len(arr),6)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
