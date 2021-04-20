#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    for i in range(n):
        ar[i]=ar[i]%k
    count=0
    for i in range(n):
        count+=ar[i+1:].count(k-ar[i])
        print(i,count)
    return count

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
