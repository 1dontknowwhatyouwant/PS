import sys
input = sys.stdin.readline
N, C = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arrlist = sorted(arr)

start = 1 
end = arrlist[-1] - arrlist[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    current = arrlist[0]
    count = 1

    for i in range(1, len(arrlist)):
        if arrlist[i] >= current + mid:
            count += 1
            current = arrlist[i]
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)