import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
path = data[1]

dp = [float('inf')] * n
dp[0] = 0

for i in range(n):
    for j in range(i + 1, n):
        if (path[i] == 'B' and path[j] == 'O') or \
           (path[i] == 'O' and path[j] == 'J') or \
           (path[i] == 'J' and path[j] == 'B'):
            cost = (j - i) ** 2
            dp[j] = min(dp[j], dp[i] + cost)

result = dp[n - 1]
print(result if result != float('inf') else -1)
