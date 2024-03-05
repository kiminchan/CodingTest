import sys

read = sys.stdin.readline
number_list = []
total = 0 

for _ in range(5):
    number = int(read())
    number_list.append(number)


number_list.sort()

 
for num in number_list:
    total += num
# 평균값
print(total//5)
# 대표값 
print(number_list[5//2])