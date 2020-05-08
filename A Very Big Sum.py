# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return sum(ar)

n = int(input())
ar = list(map(int, input().split()))
answer = aVeryBigSum(ar)
print(answer)
