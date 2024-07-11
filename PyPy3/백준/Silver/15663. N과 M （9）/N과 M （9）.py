import sys
input = sys.stdin.readline

N,M = map(int,input().split())

n = list(map(int,input().split()))
n.sort() #사전 순으로 정렬
queue = []
visited = [False]*N

def dfs():
    if len(queue) == M:
        print(*queue) 
        return
    temp = 0
    for i in range(N):
        if not visited[i] and temp != n[i]:
            visited[i] = True #방문처리
            queue.append(n[i])
            temp = n[i]
            dfs() #위에서 방문처리를 했기 때문에 접근하지 못하게 함
            visited[i] = False
            queue.pop()
            
dfs()
