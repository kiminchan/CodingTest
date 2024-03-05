# N개의 창문 N명의 사람

# 1번째 사람은 1의 배수번째 창문을 열려 있으면
# 닫고 닫혀 있으면 연다 

# 2번째 사람은 2의 배수 창문을 열려 있으면 닫고 닫혀
# 있으면 연다 
# 이러한 행동을 N번째 사람까지 진행한후
# 열려 있는 창문의 개수를 구하여라 

import sys

read = sys.stdin.readline

N = int(read())
print(int(N**0.5))
'''
windows = [0] * (N+1)
open_count = 0

for i in range(1, N+1):
    for j in range(i, N+1,i):
        if windows[j] == 0:
            windows[j] = 1
            open_count += 1
        else:
            windows[j] = 0
            open_count -=1

print(open_count)
'''
