import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i, graph, visited)
        count += 1

print(count)
