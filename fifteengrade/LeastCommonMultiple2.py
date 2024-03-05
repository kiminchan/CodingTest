import sys

read = sys.stdin.readline

def lcm(a,b):
    return (a*b) // gcd(a,b)

def gcd(a,b):
    result = 0 
    while(b != 0):
        result = a % b
        a = b 
        b = result  
    return a 

a, b = map(int,read().split())
print(lcm(a,b))



