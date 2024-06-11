import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

queue = deque(range(1, n+1))
josephus = []

while queue:
    queue.rotate(-(k-1))
    josephus.append(queue.popleft())

print('<' + ', '.join(map(str, josephus)) + '>')