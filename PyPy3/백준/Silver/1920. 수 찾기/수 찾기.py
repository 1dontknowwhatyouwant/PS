import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
sortA = sorted(A)
M = int(input())
arr = list(map(int,input().split()))

for i in arr:
    start = 0
    end = N-1
    visited = False
    while start <= end:
        mid = (start+end)//2
        if i == sortA[mid]:
            visited = True
            print(1)
            break
        elif i > sortA[mid]:
            start = mid + 1
        else:
            end = mid - 1

    if not visited:
        print(0)