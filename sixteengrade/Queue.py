import sys 
from collections import deque 
read = sys.stdin.readline

def Queue(command,queue):
    if command[0] == "push":
        queue.appendleft(int(command[1]))
    elif command[0] == "pop":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    
    elif command[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
        
    elif command[0] == "front":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    
    elif command[0] == "back":
        if queue:
            print(queue[0])
        else:
            print(-1)

N = int(read())

queue = deque()

for _ in range(N):
    command = list(read().split())
    Queue(command, queue)
