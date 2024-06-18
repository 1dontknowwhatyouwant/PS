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
            if 0 <= next_i < N and 0 <= next_j < N and not visited[next_i][next_j] and graph[next_i][next_j] == 1:
                queue.append((next_i, next_j))
                visited[next_i][next_j] = True
                count += 1

    return count

N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
answer = []

for i in range(N):
    graph.append(list(map(int, input().strip())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i, j))

answer.sort()
print(len(answer))
for num in answer:
    print(num)
