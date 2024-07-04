import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    time, pay = schedule[i]
    if i + time <= N: 
        dp[i] = max(dp[i + 1], pay + dp[i + time])
    else: 
        dp[i] = dp[i + 1]
print(dp[0])