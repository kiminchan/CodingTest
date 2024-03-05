import sys

read = sys.stdin.readline

a_one , a_two = map(int,read().split())
c = int(read())
n_zero = int(read())

if (a_one * n_zero) + a_two <= n_zero * c and  a_one <= c:
    print(1)
else: 
    print(0)
