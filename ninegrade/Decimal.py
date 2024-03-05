import sys 

read = sys.stdin.readline

M = int(read())
N = int(read())

decimal = []

for i in range(M,N+1):
    count = 0
    if i > 1:
        for j in range(2,i): 
            if i % j == 0:
                count += 1
                break
        if count == 0:
            decimal.append(i)
         
if len(decimal) == 0:
    print(-1)
else:
    print(sum(decimal))
    print(min(decimal))