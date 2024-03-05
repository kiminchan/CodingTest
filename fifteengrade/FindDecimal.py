import sys 
import math 
read = sys.stdin.readline

def is_prime(num):
    if num == 0 or num == 1:
        False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False 
        return num
M, N = map(int, read().split())

prime_list =[]

for i in range(M,N+1):
    if is_prime(i):
        prime_list.append(i)

for prime in prime_list:
    print(prime)
        