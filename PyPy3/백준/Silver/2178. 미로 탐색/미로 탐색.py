import sys
from collections import deque
input = sys.stdin.readline

def bfs_maze(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited = [[False] * m for _ in range(n)]
    
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        # 4방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
    
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip())))

print(bfs_maze(maze, n, m))

