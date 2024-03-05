import sys

read = sys.stdin.readline

N = int(read())
# 두 숫자 카드에 같은 수가 적혀있는경우는 없다. set 사용 
card = set(map(int, read().split()))

M = int(read())
number = list(map(int, read().split()))

#num_dict ={value : index for index, value in enumerate(number)}
num_dict =dict.fromkeys(number, 0)

for key in num_dict:
    num_dict[key] = 1 if key in card else 0

for value in num_dict.values():
    print(value, end=" ")








