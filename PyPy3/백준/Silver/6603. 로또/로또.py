import sys
input = sys.stdin.readline

k = 0
s = 0
queue = []
def dfs(choose,index):
    if choose == 6:
        print(*queue)
        return
    for i in range(index,k):
        queue.append(s[i])
        dfs(choose + 1,i + 1)
        queue.pop()

    
while True:
    k_list = list(map(int,input().split()))
    k = k_list[0]
    s = k_list[1:]
    dfs(0,0)
    if k == 0:
        break
    print()
