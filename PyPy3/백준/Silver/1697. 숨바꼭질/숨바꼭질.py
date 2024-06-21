import sys
from collections import deque
input = sys.stdin.readline
def bfs(start, target):
    max_pos = 100000
    visited = [False] * (max_pos + 1)
    distance = [0] * (max_pos + 1)
    
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        
        if current == target:
            return distance[current]
        
        next_positions = [current - 1, current + 1, current * 2]
        
        for next_pos in next_positions:
            if 0 <= next_pos <= max_pos and not visited[next_pos]:
                queue.append(next_pos)
                visited[next_pos] = True
                distance[next_pos] = distance[current] + 1

start, target = map(int, input().split())
print(bfs(start, target))