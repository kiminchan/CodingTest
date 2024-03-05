import sys

read = sys.stdin.readline

def StackFunction(number_list, stack):

    # 1 : 정수 X를 스택에 넣는다. 
    if number_list[0] == 1:
        stack.append(number_list[1])
    
    # 2 : 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다.
    elif number_list[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    # 3 : 스택에 들어있는 정수의 개수를 출력한다.
    elif number_list[0] == 3:
        print(len(stack))
    # 4 : 스택이 비어있으면 1, 아니면 0을 출력한다. 
    elif number_list[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    # 5 : 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력 
    elif number_list[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)

N = int(read())

stack = []

for _ in range(N):
    number_list = list(map(int,read().split()))
    StackFunction(number_list, stack)

