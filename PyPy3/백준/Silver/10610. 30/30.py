import sys
input = sys.stdin.readline

N = input().strip()

if '0' not in N:
    print(-1)

elif sum(map(int, N)) % 3 != 0:
    print(-1)

else:
    print(''.join(sorted(N, reverse=True)))