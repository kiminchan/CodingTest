import sys

read = sys.stdin.readline

n = int(read())

factorial = 1 
for i in range(1,n+1):
    factorial *=  i

print(factorial)