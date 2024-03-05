import sys

read = sys.stdin.readline

num_list = list(read().strip())

num_list.sort(reverse=True)

for num in num_list:
    print(num, end="")