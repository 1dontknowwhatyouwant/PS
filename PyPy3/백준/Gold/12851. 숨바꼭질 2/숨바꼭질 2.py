from collections import deque

def bfs(start, target):
    # 무한대를 의미하는 큰 수
    MAX = 100001
    # 방문 시간을 기록할 배열
    times = [MAX] * MAX
    # 특정 위치에 도달하는 방법의 수를 기록할 배열
    ways = [0] * MAX

    # 초기 위치의 시간을 0으로 설정하고 방법의 수는 1
    times[start] = 0
    ways[start] = 1

    # 큐 초기화
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < MAX:
                if times[next_pos] == MAX:  # 처음 방문한 경우
                    times[next_pos] = times[current] + 1
                    ways[next_pos] = ways[current]
                    queue.append(next_pos)
                elif times[next_pos] == times[current] + 1:  # 이미 방문한 적이 있지만 동일한 시간에 도달한 경우
                    ways[next_pos] += ways[current]
    
    return times[target], ways[target]

N, K = map(int, input().split())
min_time, num_ways = bfs(N, K)

print(min_time)
print(num_ways)
