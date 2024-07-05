import sys
input = sys.stdin.readline

# 테스트 케이스 수 입력 받기
T = int(input())

dp = [1]*10001

for i in range(2,10001):
    dp[i] += dp[i-2]

for i in range(3,10001):
    dp[i] += dp[i-3]

for i in range(T):
    N = int(input())
    print(dp[N])