import sys
import math


# num을 2부터 num까지 나누어서 확인 -> O(n)
# num을 2부터 num/2까지 나누어서 확인 -> O(n)
# num을 2부터 sqrt(num)까지 나누어서 확인 
# num의 약수의 중간을 구하는 원리 


# 소수인지 아닌지 판별하는 함수 
def is_prime(num):
    if num == 0 or num == 1:
        return False    
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return num

# 소수인 숫자가 나올때까지 진행 
def next_num(num):
    while True:
        if is_prime(num) == False:
            num +=1
        else:
            return num 
read = sys.stdin.readline

n = int(read())

for _ in range(n):
    num = int(read())
    print(next_num(num))




