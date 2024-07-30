import sys
input = sys.stdin.readline
def tiling_2xn(n):
    #배열 초기화
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    # 점화식을 사용하여 값 채우기
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    return dp[n]

n = int(input())
print(tiling_2xn(n)%10007)
