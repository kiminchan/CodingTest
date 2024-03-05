import sys

read = sys.stdin.readline

N = int(read())
number_list = []

for _ in range(N):
    number = int(read())
    number_list.append(number)
number_list.sort()

for num in number_list:
    print(num)
