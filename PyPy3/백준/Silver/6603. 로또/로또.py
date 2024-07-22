import sys
input = sys.stdin.readline

k = 0
s = 0
prn = []
def dfs(queue,index):
    if queue == 6:
        print(*prn)
        return
    for i in range(index,k):
        prn.append(s[i])
        dfs(queue + 1,i + 1)
        prn.pop()

    
while True:
    k_list = list(map(int,input().split()))
    k = k_list[0]
    s = k_list[1:]
    dfs(0,0)
    if k == 0:
        break
    print()
    