import sys 
from collections import Counter 
read = sys.stdin.readline

# 상근이가 가지고 있는 숫자 카드 개수 
N = int(read())
sang_number = list(map(int, read().split()))

# 주어진 카드 개수 
M = int(read())
number = list(map(int, read().split()))

counter = Counter(sang_number)

for num in number:
    print(counter[num], end=" ")


'''
# 시간 초과 
result = [sang_number.count(num) if sang_number.count(num) != 0 else 0 for num in number]

for num in result:
    print(num, end =" ")
'''