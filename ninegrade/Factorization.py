import sys

read = sys.stdin.readline

N = int(read())

list = []
decimal_list = []

for i in range(1,N+1):
    if N % i== 0:
        list.append(i)

for num in list:
    error = 0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                error += 1 
        
        if error == 0:
            decimal_list.append(num)
demical = []

while True:
    if N == 1: 
        break
    for num in decimal_list:
        if N % num == 0:
            N = N/num
            demical.append(num)
demical.sort()

for num in demical:
    print(num)

