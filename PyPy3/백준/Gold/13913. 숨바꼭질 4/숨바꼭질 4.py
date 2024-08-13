import sys
from collections import deque
input = sys.stdin.readline

def bfs(N, K):
    MAX = 100000
    visited = [-1] * (MAX + 1)
    queue = deque([N])
    visited[N] = N

    while queue:
        current = queue.popleft()

        if current == K:
            break

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= MAX and visited[next_pos] == -1:
                queue.append(next_pos)
                visited[next_pos] = current

    path = []
    while K != N:
        path.append(K)
        K = visited[K]
    path.append(N)
    path.reverse()

    return path

N, K = map(int, input().split())

print(len(bfs(N,K)) - 1)
print(' '.join(map(str, bfs(N,K))))
