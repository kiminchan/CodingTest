import sys

read = sys.stdin.readline

N = int(read())

num_list = []
for _ in range(N):
    num = int(read())
    num_list.append(num)

num_list.sort()

for n in num_list:
    print(n)