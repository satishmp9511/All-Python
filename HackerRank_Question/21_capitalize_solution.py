import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a=s.split(" ")
    f=""
    for i in a:
        p=i.capitalize()
        f=f+p+" "
        
    return f

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
