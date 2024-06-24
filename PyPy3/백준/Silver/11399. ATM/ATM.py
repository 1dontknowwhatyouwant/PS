import sys
input = sys.stdin.readline

N = int(input())
person = list(map(int,input().split()))
person.sort()

answer = 0

for i in range(1,N+1):
    answer += sum(person[0:i])

print(answer)