import sys 
from collections import deque 

read= sys.stdin.readline

N = int(read())

list = [i for i in range(1,N+1)]

list = deque(list)

while len(list) != 1:
    list.popleft()
    list.append(list.popleft())

print(list[0])