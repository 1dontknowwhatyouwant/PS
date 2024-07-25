import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
colorGraph = [list(input()) for _ in range(M)]
x_move = [0,1,0,-1]
y_move = [1,0,-1,0]
white,blue = 0,0

def bfs(x,y,color):
    count = 0
    queue = deque([])
    queue.append((x,y))
    colorGraph[x][y] = 0

    while queue:
        x,y = queue.popleft()
        count += 1
        for i in range(4):
            dx = x + x_move[i]
            dy = y + y_move[i]
            if 0 <= dx < M and 0 <= dy < N:
                if colorGraph[dx][dy] == color:
                    queue.append((dx,dy))
                    colorGraph[dx][dy] = 0

    return count

for i in range(M):
    for j in range(N):
        if colorGraph[i][j] == 'W':
            white += (bfs(i,j,'W'))**2
        elif colorGraph[i][j] == 'B':
            blue += (bfs(i,j,'B'))**2

print(white,blue)