import sys
input = sys.stdin.readline
# 방향: 북 (0), 동 (1), 남 (2), 서 (3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move_turtle(commands):
    x, y, direction = 0, 0, 0
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    
    for command in commands:
        if command == 'F':
            x += dx[direction]
            y += dy[direction]
        elif command == 'B':
            x -= dx[direction]
            y -= dy[direction]
        elif command == 'L':
            direction = (direction + 3) % 4
        elif command == 'R':
            direction = (direction + 1) % 4
        
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    return (max_x - min_x) * (max_y - min_y)

t = int(input())
for _ in range(t):
    commands = input().strip()
    print(move_turtle(commands))
