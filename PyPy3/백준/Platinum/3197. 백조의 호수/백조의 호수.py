import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, input().split())
lake = []
water_queue = deque()
swan_positions = []

# 지도 입력
for i in range(R):
    row = list(input().strip())
    lake.append(row)
    for j in range(C):
        if lake[i][j] == 'L':
            swan_positions.append((i, j))
            lake[i][j] = '.'  # 백조가 있는 자리는 물로 간주
        if lake[i][j] == '.':
            water_queue.append((i, j))

# 백조의 BFS를 위한 큐와 방문 표시
swan_queue = deque([swan_positions[0]])
visited_swan = [[False] * C for _ in range(R)]
visited_swan[swan_positions[0][0]][swan_positions[0][1]] = True

# 백조가 만났는지 확인하기 위한 함수
def is_swan_met():
    next_swan_queue = deque()
    while swan_queue:
        x, y = swan_queue.popleft()
        if (x, y) == swan_positions[1]:
            return True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited_swan[nx][ny]:
                visited_swan[nx][ny] = True
                if lake[nx][ny] == '.':
                    swan_queue.append((nx, ny))
                else:
                    next_swan_queue.append((nx, ny))
    swan_queue.extend(next_swan_queue)
    return False

# 얼음을 녹이기 위한 함수
def melt_ice():
    next_water_queue = deque()
    while water_queue:
        x, y = water_queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == 'X':
                lake[nx][ny] = '.'
                next_water_queue.append((nx, ny))
    return next_water_queue

days = 0
while not is_swan_met():
    days += 1
    water_queue = melt_ice()

print(days)
