import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int,input().split()))
sortX = sorted(set(X)) # 중복 삭제,정렬
dictionaryX = {sortX[i]:i for i in range(len(sortX))}

for i in X:
    print(dictionaryX[i],end=" ")