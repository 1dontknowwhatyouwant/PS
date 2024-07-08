import sys
input = sys.stdin.readline

def count_papers(x, y, n): #분할정복 알고리즘 사용
    initial = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != initial:
                new_n = n // 3
                count_papers(x, y, new_n)
                count_papers(x, y + new_n, new_n)
                count_papers(x, y + 2 * new_n, new_n)
                count_papers(x + new_n, y, new_n)
                count_papers(x + new_n, y + new_n, new_n)
                count_papers(x + new_n, y + 2 * new_n, new_n)
                count_papers(x + 2 * new_n, y, new_n)
                count_papers(x + 2 * new_n, y + new_n, new_n)
                count_papers(x + 2 * new_n, y + 2 * new_n, new_n)
                return
    if initial == -1:
        counts[0] += 1
    elif initial == 0:
        counts[1] += 1
    elif initial == 1:
        counts[2] += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
counts = [0, 0, 0]  # -1, 0, 1의 개수를 셀 리스트


count_papers(0, 0, n)

for count in counts:
    print(count)