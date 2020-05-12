#!/bin/python3

import os

# Complete the plusMinus function below.
def plusMinus(arr):
    p=neg=z=0
    for i in arr:
        if i>0:
            p=p+1
        elif i<0:
            neg=neg+1
        else:
            z=z+1
    print(p/n)
    print(round(neg/n,6))
    print(round(z/n,6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
