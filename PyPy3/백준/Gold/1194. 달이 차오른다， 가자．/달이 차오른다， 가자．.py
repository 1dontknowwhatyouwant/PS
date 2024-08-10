import sys
input = sys.stdin.readline
from collections import deque

def bfs(maze, start, n, m):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    queue = deque([(start[0], start[1], 0, 0)])
    visited = [[[False] * (1 << 6) for _ in range(m)] for _ in range(n)]
    visited[start[0]][start[1]][0] = True
    
    while queue:
        x, y, keys, steps = queue.popleft()
      
        if maze[x][y] == '1':
            return steps
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                cell = maze[nx][ny]
                if cell == '#':
                    continue                
                new_keys = keys
                if 'a' <= cell <= 'f':
                    new_keys |= (1 << (ord(cell) - ord('a')))
                
                if 'A' <= cell <= 'F' and not (new_keys & (1 << (ord(cell) - ord('A')))):
                    continue
                
                if not visited[nx][ny][new_keys]:
                    visited[nx][ny][new_keys] = True
                    queue.append((nx, ny, new_keys, steps + 1))
    
    return -1

n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]

start = None
for i in range(n):
    for j in range(m):
        if maze[i][j] == '0':
            start = (i, j)
            break
    if start:
        break

result = bfs(maze, start, n, m)
print(result)
