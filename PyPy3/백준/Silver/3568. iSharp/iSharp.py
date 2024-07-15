import sys
input = sys.stdin.readline

string = input().replace(",", '').replace(";", '').split()
temp = string.pop(0)

for i in string:
    print(temp,end = '')
    
    for j in range(len(i)-1,0,-1):
        if not i[j].isalpha():
            if i[j] == ']':
                print('[',end='')
            elif i[j] == '[':
                print(']',end='')
            else:
                print(i[j],end='')

    print(' ',end='')
    for j in range(len(i)):
        if i[j].isalpha():
            print(i[j],end='')

    print(";")