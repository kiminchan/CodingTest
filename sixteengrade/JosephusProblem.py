# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있다 

# 순서대로 K번째 사람을 제거한다. 

# 한 사람이 제거 되면 남은 사람들로 이루어진 원을 따라 과정 계속 반복 

# N명의 사람이 모두 제거될 떄까지 계속 

# 제거되는 순서를 (N,K) 요세푸스 순열
import sys 

read = sys.stdin.readline

N, K = map(int, read().split())
 

queue = [i for i in range(1, N+1)]
Josephus_list = []
rear = K-1

while len(queue) != 0:
        rear %= len(queue)
        Josephus_list.append(queue.pop(rear))
        rear += K-1

count = 1
print("<", end="")
for idx in Josephus_list:
    if count == len(Josephus_list):
        print(str(idx), end="")
    else:
        print(str(idx)+", ", end="")
        count +=1
print(">") 

# <3, 6, 2, 7, 5, 1, 4>
# <3, 6, 2, 7, 5, 1, 4>