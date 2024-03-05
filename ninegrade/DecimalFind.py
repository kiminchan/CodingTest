import sys 

read = sys.stdin.readline

N = int(read())
count = 0
decimal = []
decimal = list(map(int,read().split()))

for num in decimal:
    error = 0
    if num > 1 :
        for i in range(2,num):
            if num % i == 0:
                error +=1 
                break
        if error == 0:
            count +=1

print(count)
        
    
