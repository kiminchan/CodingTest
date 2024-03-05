import sys


def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)
    
read = sys.stdin.readline

n = int(read())

print(factorial(n))