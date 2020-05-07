#Code:

import os

def compareTriplets(a, b):
    c=0
    d=0
    i=0
    while i!=3:
        if a[i]>b[i]:
            c=c+1
        elif a[i]<b[i]:
            d=d+1
        i=i+1
    return c,d
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
