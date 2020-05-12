#!/bin/python3

import os


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    a=[]
    b=[]
    mini=ax=0
    c= arr.pop()
    for i in arr:
        mini=mini+i
    arr.append(c)
    arr.sort(reverse=True)
    arr.pop()
    for i in arr:
        ax=ax+i
    print(mini,ax)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
