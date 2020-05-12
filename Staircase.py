#!/bin/python3

import os


# Complete the staircase function below.
def staircase(n):
    i=n-1
    while i!=-1:
        j=n-i
        print(' '*i+'#'*j)
        i=i-1
        j=j+1


if __name__ == '__main__':
    n = int(input())

    staircase(n)
