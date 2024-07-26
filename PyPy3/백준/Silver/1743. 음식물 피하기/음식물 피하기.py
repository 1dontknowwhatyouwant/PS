import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    count = 0
    queue = deque([])
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        x,y = queue.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))

    return count
            
N,M,K = map(int,input().split())
graph = [[0] * M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 1

for _ in range(K):
    r,c = map(int,input().split())
    graph [r-1][c-1] = 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            answer = max(answer,bfs(i,j))

print(answer)
