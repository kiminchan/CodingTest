import sys
import math 
read = sys.stdin.readline

# n보다 크고 2n보다 작거나 같은 범위 
# +1은 리스트 첫번째 사용 안하므로 
num = 123456*2 + 1
num_list = [1] * num

for i in range(1,num):
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i)) + 1):
        # 소수가 아니다
        if i % j == 0:
            num_list[i] = 0
            break

while True:
    num = int(read())
    if num == 0:
        break 
    prime = 0
    for i in range(num+1, (2*num)+1):
        prime += num_list[i]
    print(prime)
    
        
    
