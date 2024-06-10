import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    stackWord = sys.stdin.readline().split()

    if stackWord[0]=='push': #삽입
        stack.append(stackWord[1])
    elif stackWord[0]=='pop': #맨 위 값을 삭제하고 출력
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif stackWord[0]=='size': #스택에 들어있는 정수의 개수
        print(len(stack))
    elif stackWord[0]=='empty': #스택이 비어있는지 테스트
        if len(stack)==0:
            print(1)
        else:
            print(0)

    elif stackWord[0]=='top': #가장 위에 있는 원소 출력
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])