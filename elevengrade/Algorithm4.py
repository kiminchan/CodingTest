import sys 

read = sys.stdin.readline

n = int(read())

degree =0 
for i in range(1,n):
    degree += i

print(degree)
print(2)