import sys
from collections import deque

input = sys.stdin.readline

def bfs(start1, start2):
    queue = deque([(start1, start2)])
    visited[start1][start2] = True
    count = 1

    while queue:
        currenti, currentj = queue.popleft()
        for xyi, xyj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_i, next_j = currenti + xyi, currentj + xyj
            if 0 <= next_i < N and 0 <= next_j < M and not visited[next_i][next_j] and graph[next_i][next_j] == 1:
                queue.append((next_i, next_j))
                visited[next_i][next_j] = True
                count += 1

    return count

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)
