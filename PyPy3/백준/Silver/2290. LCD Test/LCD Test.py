import sys
input = sys.stdin.readline
def lcd_display(s, n):
    # 각 숫자에 대한 세그먼트 배열 (가로-세로-가로-세로-가로 순서로 나열)
    segments = {
        '0': [' - ', '| |', '   ', '| |', ' - '],
        '1': ['   ', '  |', '   ', '  |', '   '],
        '2': [' - ', '  |', ' - ', '|  ', ' - '],
        '3': [' - ', '  |', ' - ', '  |', ' - '],
        '4': ['   ', '| |', ' - ', '  |', '   '],
        '5': [' - ', '|  ', ' - ', '  |', ' - '],
        '6': [' - ', '|  ', ' - ', '| |', ' - '],
        '7': [' - ', '  |', '   ', '  |', '   '],
        '8': [' - ', '| |', ' - ', '| |', ' - '],
        '9': [' - ', '| |', ' - ', '  |', ' - '],
    }

    # 숫자를 세로로 확장하기
    digits = [segments[digit] for digit in n]
    rows = []

    # 첫 가로 줄
    rows.append(' '.join(d[0][0] + d[0][1]*s + d[0][2] for d in digits))

    # 첫 세로 줄
    for _ in range(s):
        rows.append(' '.join(d[1][0] + d[1][1]*s + d[1][2] for d in digits))

    # 중간 가로 줄
    rows.append(' '.join(d[2][0] + d[2][1]*s + d[2][2] for d in digits))

    # 두번째 세로 줄
    for _ in range(s):
        rows.append(' '.join(d[3][0] + d[3][1]*s + d[3][2] for d in digits))

    # 마지막 가로 줄
    rows.append(' '.join(d[4][0] + d[4][1]*s + d[4][2] for d in digits))

    # 결과
    for row in rows:
        print(row)


s, n = input().split()
s = int(s)
lcd_display(s, n)

