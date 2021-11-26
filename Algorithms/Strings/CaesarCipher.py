#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    ciphered_message = ""
    for characters in s:
        char_value = ord(characters)
        if (char_value < 65 or char_value > 90) and (char_value < 97 or char_value > 122) :
            char_value = char_value
        else: 
            if characters.islower():
                first_letter = ord('a')
            else:
                first_letter = ord('A')

            char_value = ((ord(characters) - first_letter + k) % 26 ) + first_letter
        ciphered_message = ciphered_message + chr(char_value)
        
        
    return ciphered_message

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
