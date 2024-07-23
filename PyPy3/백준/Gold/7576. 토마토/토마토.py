import sys
from collections import deque
input = sys.stdin.readline
x = [-1,0,1,0]
y = [0,1,0,-1]

M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
queue = deque([])

answer = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i,j])

def bfs():
    while queue:
        dx,dy = queue.popleft()
        for i in range(4):
            nx,ny = x[i]+dx, y[i]+dy
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[dx][dy] + 1
                queue.append([nx,ny])

bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer,max(i))

print(answer - 1)