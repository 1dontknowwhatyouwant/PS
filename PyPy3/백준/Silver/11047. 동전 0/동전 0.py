import sys
input = sys.stdin.readline

N,K = map(int,input().split())
count = 0
coin = []
for _ in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)

for i in coin:
    if K == 0:
        break;
    count += K // i
    K %= i
    
print(count)
