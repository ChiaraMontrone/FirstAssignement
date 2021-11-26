#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] =='PM':
    
        if s[:2] != '12':
            hs = int(s[:2])+12
        else:
            hs = s[:2]

    else:
        if s[:2] == '12':
            hs = '00'
        else:
            hs = s[:2]
    s= str(hs) + s[2:8]   
    return s    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
