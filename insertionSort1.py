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
    # Write your code here
    for i in range(1,n):
        j=i-1
        current = arr[i]
        while current < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j-=1
            for m in arr:
                print(m, end=' ')
            print()
        arr[j+1] = current
    for m in arr:
        print(m, end=' ')
    print()
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
