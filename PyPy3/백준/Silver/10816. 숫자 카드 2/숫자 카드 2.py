import sys
input = sys.stdin.readline

N = int(input().strip())
intN = sorted(list(map(int,input().strip().split())))

M = int(input().strip())
intM = list(map(int,input().strip().split()))

dictionaryN = {}
for N in intN:
    if N in dictionaryN:
        dictionaryN[N] += 1
    else:
        dictionaryN[N] = 1

def binary(M,intN,start,end):
    if start > end:
        return 0
    mid = (start + end)//2
    if M == intN[mid]:
        return dictionaryN[M]
    elif M < intN[mid]:
        return binary(M,intN,start,mid-1)
    else:
        return binary(M,intN,mid+1,end)
    
for M in intM:
    print(binary(M,intN,0,len(intN)-1),end=" ")