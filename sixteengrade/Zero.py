import sys

read = sys.stdin.readline

K = int(read())

num_list = []
total = 0
for i in range(K):
    num = int(read())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)

for num in num_list:
    total += num

print(total)


