#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    counter_num =  0
    count_lc = 0
    count_uc = 0
    count_sc = 0

    min = 0

    for i in password:
        if i in numbers:
            counter_num  = 1                
        if i in  lower_case:
            count_lc = 1
        if i in  upper_case:
            count_uc = 1
        if i in  special_characters:
            count_sc = 1
        min = 4 - count_sc -count_lc - count_uc -counter_num

    if min > (6 -n):
        return  min
    else:
        return (6-n )
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
