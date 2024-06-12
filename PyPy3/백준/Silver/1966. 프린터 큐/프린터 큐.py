from collections import deque
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    queue = deque(queue)
    
    result = 1
    while queue:
        if queue[0] < max(queue):
            queue.append(queue.popleft())

        else:
            if m == 0: break

            queue.popleft()
            result += 1

        if m == 0:
            m = len(queue) - 1
        else:
            m -= 1

    print(result)