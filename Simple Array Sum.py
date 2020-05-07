#Given an array of integers, find the sum of its elements.
#Code:

import os
import sys

def simpleArraySum(ar):
    c=0
    for i in ar:
        c=c+i
    print(c)
ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = simpleArraySum(ar)
