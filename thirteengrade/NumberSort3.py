import sys

read = sys.stdin.readline

n = int(read())
num_list = [0] * 10001
for _ in range(n):
    num = int(read())
    num_list[num] += 1

for i in range(len(num_list)):
    if i != 0:
        for j in range(num_list[i]):
            print(i)
    
