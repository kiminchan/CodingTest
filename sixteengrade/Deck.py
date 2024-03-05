import sys 
from collections import deque 

def Deck(command, deck):
    # 1 x : 정수 X를 덱의 앞에 넣는다. 
    if command[0] == '1':
        deck.appendleft(int(command[1]))
    # 2 x : 정수 X를 덱의 뒤에 넣는다. 
    elif command[0] == '2':
        deck.append(int(command[1]))

    # 3 : 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력, 없다면 -1 
    elif command[0] == '3':
        if isEmpty(deck):
            print(deck.popleft())
        else:
            print(-1)
    # 4 : 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력 , 없다면 -1
    elif command[0] == '4':
        if isEmpty(deck):
            print(deck.pop())
        else:
            print(-1)
    # 5 : 덱에 들어있는 정수의 개수를 출력
    elif command[0] =='5':
        print(len(deck))
    
    # 6 : 덱이 비어있으면 1 아니면 0을 출력 
    elif command[0] =='6':
        if isEmpty(deck):
            print(0)
        else:
            print(1)
    # 7 : 덱에 정수가 있다면 맨 앞의 정수를 출력 , 없다면 -1 
    elif command[0] == '7':
        if isEmpty(deck):
            print(deck[0])
        else:
            print(-1)
    # 8 : 덱에 정수가 있다면 맨 뒤의 정수를 출력 , 없다면 -1 
    elif command[0] == '8':
        if isEmpty(deck):
            print(deck[-1])
        else:
            print(-1)

# 덱이 비어있는지 아닌지 확인하는 함수 
def isEmpty(deck):
    if deck:
        return True
    else:
        return False

read = sys.stdin.readline

deck = deque()

N = int(read())

for _ in range(N):
    command = list(read().split())
    Deck(command,deck)
