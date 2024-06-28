import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
team = min(N // 2, M)
remainStudent = (N - team * 2) + (M - team)

while remainStudent < K:
    team -= 1
    remainStudent += 3 

print(team)
