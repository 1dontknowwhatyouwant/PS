n,m = map(int,input().split())
tree = list(map(int,input().split()))

left = 0
right = max(tree)

while left<=right:
    mid = (left+right)//2
    total = 0
    for i in tree:
        if i > mid:
            total += i - mid

    if total < m:
        right = mid - 1
    else:
        left = mid + 1


print(right)
        