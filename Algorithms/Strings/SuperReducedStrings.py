#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    a=0
    while a < len(s)-1:
        if s[a] == s[a + 1]:
            s = s[0 : a : ] + s[a + 2: :]
            s = superReducedString(s)
        else:
            a=a+1
    if len(s) == 0:
        s = 'Empty String'
    return s
    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
