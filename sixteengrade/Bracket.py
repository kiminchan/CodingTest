# 괄호 문자열은 두 개의 괄호 기호인 "(" ,")"만으로 구성되어 있는 문자열
# 올바르게 구성된 문자열을 VPS
import sys

read = sys.stdin.readline

N = int(read())

VPS = []

for _ in range(N):
    string = list(read())

    count = 0
    for idx in string:
        if idx == '(':
            count +=1
        elif idx == ')':
            count -= 1

        if count < 0:
            print('NO')
            break
    
    if count > 0:
        print('NO')
    elif count == 0:
        print('YES')
