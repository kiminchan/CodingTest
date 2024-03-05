# 1번부터 N번까지 N개의 풍선이 원형으로 놓여있음
# i번 풍선의 오른쪽에는 i+1번 풍선 왼쪽에는 i-1풍선이 있음
# 단, 1번의 풍선의 왼쪽에는 N번 풍선이 있고 N번 풍선의 오른쪽에는
# 1번 풍선이 있다. 
# 이 풍선들을 다음과 같은 규칙으로 터뜨린다 

# 제일 처음에는 1번 풍선을 터뜨린다
# 다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼
# 이동하여 다음 풍선을 터뜨린다 

# 다섯개의 풍선 안에 차례로 3,2,1,-3,-1이 적혀 있음
import sys 
from collections import deque 
read = sys.stdin.readline

N = int(read())

# 1부터 N까지 풍선 번호 
balloon = [i for i in range(1,N+1)]

# 풍선이 터진 순서 번호 
balloon_pops =[]

# 풍선안에 들어있는 값 
balloon_list = list(map(int, read().split()))

front = 0
temp = balloon_list.pop(front)
balloon_pops.append(balloon.pop(front))

while balloon_list:
    if temp < 0:
        front = (front+temp)%len(balloon_list)
    else:
        front = (front+temp-1)%len(balloon_list)
    temp = balloon_list.pop(front)
    balloon_pops.append(balloon.pop(front))

for i in balloon_pops:
    print(i , end=" ")


