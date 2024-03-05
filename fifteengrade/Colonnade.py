import sys 
from math import gcd 
read = sys.stdin.readline

# 가로등의 개수 
N = int(read())

# 첫 가로수 위치 
a = int(read())

# 가로수 사이의 값들을 저장한 리스트 
length = []

for i in range(N-1):
    num = int(read())
    length.append(num-a)
    a = num

# length에 들어있는 모든수들의 최대 공약수 찾기
g = length[0]

for i in range(1, len(length)):
    g = gcd(g, length[i])

# 둘 사이에 심을 가로수 개수 : 간격 // 최대 공약수 -1 
result = 0
for item in length:
    result += item // g -1 
print(result)
