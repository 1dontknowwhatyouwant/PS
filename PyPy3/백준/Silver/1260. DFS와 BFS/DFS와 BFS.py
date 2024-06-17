import sys
from collections import deque
def dfs(v):
    global visited
    visited[v] = True
    print(v,end = ' ')
    for next in range(1,N+1):
        if not visited[next] and graph[v][next]:
            dfs(next)

def bfs(v):
    global queue,visited
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v,end = ' ')
        for next in range(1,N+1):
            if not visited[next] and graph[v][next]:
                visited[next] = True
                queue.append(next)

input = sys.stdin.readline
N,M,V = map(int,input().split())
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

dfs(V)
print()
visited = [False] * (N+1)
queue = [V]
visited[V] = True
bfs(V)