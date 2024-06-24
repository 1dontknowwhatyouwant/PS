import sys
input = sys.stdin.readline

N = int(input())
I = []
for _ in range(N):
    start,finish = map(int,input().split())
    I.append((start,finish))

I.sort(key=lambda x : (x[1],x[0]))
count = 0
finish = I[0][0]

for i in range(N):
    if I[i][0]>=finish:
        finish = I[i][1]
        count += 1
print(count)