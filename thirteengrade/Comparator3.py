'''
import sys
read = sys.stdin.readline
N = int(read())

X = list(map(int, read().split()))

idx_x = set(X)
idx_x = list(idx_x)
idx_x.sort()

result =[]

for i in range(N):
    if idx_x.index(X[i]) != -1:
        result.append(idx_x.index(X[i]))

for item in result:
    print(item, end=" ")
'''

import sys 

read = sys.stdin.readline

N=int(read())

X = list(map(int, read().split()))
# set(X) : X의 중복요소 제거 
# sorted(X) : 오름차순 정렬 
# enumerate(X) : 요소를 열거하여 인덱스와 값 모두 제공 
idx_dict ={value: index for index, value in enumerate(sorted(set(X)))}

# 각 X의 각 요소 'x'에 대해 'idx_dict'사전에서 해당 인덱스
# 찾아 추가하는 리스트를 생성 
result = [idx_dict[x] for x in X]

for item in result:
    print(item, end=" ")


