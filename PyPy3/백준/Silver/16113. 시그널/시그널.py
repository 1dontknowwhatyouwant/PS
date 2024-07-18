import sys
input = sys.stdin.readline

N = int(input())
C = N//5
S = input().rstrip()
graph = [list(S[i*C:(i+1)*C]) for i in range(5)]
col = 0
while True:
    try:
        if (graph[0][col] == '#' and graph[0][col+1] == '.' and 
            graph[1][col] == '#' and graph[1][col+1] == '.' and 
            graph[2][col] == '#' and graph[2][col+1] == '.' and 
            graph[3][col] == '#' and graph[3][col+1] == '.' and
            graph[4][col] == '#' and graph[4][col+1] == '.'):
            print(1, end = '')
            col += 2
        elif (graph[0][col] == '#' and graph[0][col+1] == '#' and graph[0][col+2] == '#' and
              graph[1][col] == '#' and graph[1][col+1] == '.' and graph[1][col+2] == '#' and
              graph[2][col] == '#' and graph[2][col+1] == '.' and graph[2][col+2] == '#' and
              graph[3][col] == '#' and graph[3][col+1] == '.' and graph[3][col+2] == '#' and
              graph[4][col] == '#' and graph[4][col+1] == '#' and graph[4][col+2] == '#'):
            print(0, end = '')
            col += 4
        elif (graph[0][col] == '#' and graph[0][col+1] == '#' and graph[0][col+2] == '#' and
              graph[1][col] == '.' and graph[1][col+1] == '.' and graph[1][col+2] == '#' and
              graph[2][col] == '#' and graph[2][col+1] == '#' and graph[2][col+2] == '#' and
              graph[3][col] == '#' and graph[3][col+1] == '.' and graph[3][col+2] == '.' and
              graph[4][col] == '#' and graph[4][col+1] == '#' and graph[4][col+2] == '#'):
            print(2, end = '')
            col += 4
        elif (graph[0][col] == '#' and graph[0][col+1] == '#' and graph[0][col+2] == '#' and
              graph[1][col] == '.' and graph[1][col+1] == '.' and graph[1][col+2] == '#' and
              graph[2][col] == '#' and graph[2][col+1] == '#' and graph[2][col+2] == '#' and
              graph[3][col] == '.' and graph[3][col+1] == '.' and graph[3][col+2] == '#' and
              graph[4][col] == '#' and graph[4][col+1] == '#' and graph[4][col+2] == '#'):
            print(3, end = '')
            col += 4
        elif (graph[0][col] == '#' and graph[0][col+1] == '.' and graph[0][col+2] == '#' and
              graph[1][col] == '#' and graph[1][col+1] == '.' and graph[1][col+2] == '#' and
              graph[2][col] == '#' and graph[2][col+1] == '#' and graph[2][col+2] == '#' and
              graph[3][col] == '.' and graph[3][col+1] == '.' and graph[3][col+2] == '#' and
              graph[4][col] == '.' and graph[4][col+1] == '.' and graph[4][col+2] == '#'):
            print(4, end = '')
            col += 4
        elif (graph[0][col] == '#' and graph[0][col+1] == '#' and graph[0][col+2] == '#' and
              graph[1][col] == '#' and graph[1][col+1] == '.' and graph[1][col+2] == '.' and
              graph[2][col] == '#' and graph[2][col+1] == '#' and graph[2][col+2] == '#' and
              graph[3][col] == '.' and graph[3][col+1] == '.' and graph[3][col+2] == '#' and
              graph[4][col] == '#' and graph[4][col+1] == '#' and graph[4][col+2] == '#'):
            print(5, end = '')
            col += 4
        elif (graph[0][col] == '#' and graph[0][col+1] == '#' and graph[0][col+2] == '#' and
              graph[1][col] == '#' and graph[1][col+1] == '.' and graph[1][col+2] == '.' and
              graph[2][col] == '#' and graph[2][col+1] == '#' and graph[2][col+2] == '#' and
              graph[3][col] == '#' and graph[3][col+1] == '.' and graph[3][col+2] == '#' and
              graph[4][col] == '#' and graph[4][col+1] == '#' and graph[4][col+2] == '#'):
            print(6, end = '')
            col += 4
        elif (graph[0][col] == '#' and graph[0][col+1] == '#' and graph[0][col+2] == '#' and
              graph[1][col] == '.' and graph[1][col+1] == '.' and graph[1][col+2] == '#' and
              graph[2][col] == '.' and graph[2][col+1] == '.' and graph[2][col+2] == '#' and
              graph[3][col] == '.' and graph[3][col+1] == '.' and graph[3][col+2] == '#' and
              graph[4][col] == '.' and graph[4][col+1] == '.' and graph[4][col+2] == '#'):
            print(7, end = '')
            col += 4
        elif (graph[0][col] == '#' and graph[0][col+1] == '#' and graph[0][col+2] == '#' and
              graph[1][col] == '#' and graph[1][col+1] == '.' and graph[1][col+2] == '#' and
              graph[2][col] == '#' and graph[2][col+1] == '#' and graph[2][col+2] == '#' and
              graph[3][col] == '#' and graph[3][col+1] == '.' and graph[3][col+2] == '#' and
              graph[4][col] == '#' and graph[4][col+1] == '#' and graph[4][col+2] == '#'):
            print(8, end = '')
            col += 4
        elif (graph[0][col] == '#' and graph[0][col+1] == '#' and graph[0][col+2] == '#' and
              graph[1][col] == '#' and graph[1][col+1] == '.' and graph[1][col+2] == '#' and
              graph[2][col] == '#' and graph[2][col+1] == '#' and graph[2][col+2] == '#' and
              graph[3][col] == '.' and graph[3][col+1] == '.' and graph[3][col+2] == '#' and
              graph[4][col] == '#' and graph[4][col+1] == '#' and graph[4][col+2] == '#'):
            print(9, end = '')
            col += 4
        else:
            col += 1
    except IndexError:
        if ((col == C-1) and
            graph[0][col] == '#' and
            graph[1][col] == '#' and 
            graph[2][col] == '#' and 
            graph[3][col] == '#' and 
            graph[4][col] == '#') :
            print(1, end = '')
        elif ((col == C-2) and
              graph[0][col] == '.' and graph[0][col] == '#' and
              graph[1][col] == '.' and graph[1][col] == '#' and
              graph[2][col] == '.' and graph[2][col] == '#' and
              graph[3][col] == '.' and graph[3][col] == '#' and
              graph[4][col] == '.' and graph[4][col] == '#'):
            print(1, end = '')
        elif ((col == C-2) and
              graph[0][col] == '#' and graph[0][col] == '.' and
              graph[1][col] == '#' and graph[1][col] == '.' and
              graph[2][col] == '#' and graph[2][col] == '.' and
              graph[3][col] == '#' and graph[3][col] == '.' and
              graph[4][col] == '#' and graph[4][col] == '.'):
            print(1, end = '')
        break