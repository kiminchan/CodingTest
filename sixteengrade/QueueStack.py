import sys
from collections import deque 
read = sys.stdin.readline

# queuestack을 구성하는 자료구조의 개수 N 
N = int(read())

# queue 인지 stack인지 확인
Isqueuestack = list(map(int, read().split()))

# 자료구조에 들어가있는 원소
basic = list(map(int,read().split()))

# 삽입할 문자열 길이 
M = int(read())

# 삽입할 원소를 담고 있는 길이 M의 수열 C 
C = list(map(int, read().split()))

queue = deque()

for i  in range(N):
    if Isqueuestack[i] == 0:
        queue.append(basic[i])

for i in C:
    queue.appendleft(i)
    print(queue.pop(), end=" ")
'''
# queuestack에 삽입할때 나오는 결과 값
result =[]
queue = deque()
stack = []
# 1. Isqueuestack을 사용해서 0이면 queue , 1이면 stack 자료구조를 생성 
for i in range(len(Isqueuestack)):
    # 2. 자료구조를 생성하면 해당 자료구조에 basic 리스트의 값들을 삽입 
    if Isqueuestack[i] == 0:
        queue.appendleft(basic[i])
    else:
        stack.append(basic[i])
# 3. 총 M번(삽입할 문자열 길이)반복 진행하며 N의 개수만큼 자료구조들을 
# 1번 부터 N까지의 자료구조에서 패턴 반복 
x = 0
for i in range(M):
    x = C[i]
    for j in range(N):
        #queue 
        if Isqueuestack[j] == 0:
            queue.appendleft(x)
            x = queue.pop()
        #stack
        else:
            stack.append(x)
            x = stack.pop()
    # 4. 결과값들은 result에 저장 
    result.append(x)

for idx in result:
    print(idx, end=" ")
'''
