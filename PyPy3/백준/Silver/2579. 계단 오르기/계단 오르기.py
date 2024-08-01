import sys
input = sys.stdin.readline

T = int(input())
stair = [0] * 1000
for i in range(1, T + 1):
    stair[i] = int(input())

dp = [0] * 1000
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3],stair[2] + stair[3])

for i in range(4,T + 1):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])


print(dp[T])