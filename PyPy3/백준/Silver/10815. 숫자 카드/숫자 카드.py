import sys
input = sys.stdin.readline

N = int(input())
intN = sorted(list(map(int,input().strip().split())))
M = int(input())
intM = list(map(int,input().split()))

def binary(M,intN,start,end):
    if start > end:
        return 0
    mid = (start + end)//2
    if intN[mid] == M:
        return 1
    elif M < intN[mid]:
        return binary(M,intN,start,mid-1)
    else:
        return binary(M,intN,mid+1,end)
        
for M in intM:
    print(binary(M,intN,0,len(intN)-1),end=" ")