import sys 

read = sys.stdin.readline

N = int(read())

total = 0 
number = read()
numbers = [char for char in number]

for i in range(N):
    total += int(numbers[i])

print(total)