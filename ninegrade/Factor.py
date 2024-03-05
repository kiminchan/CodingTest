import sys

read = sys.stdin.readline

N, K = map(int,read().split())

factor = []
count = 0 

for i in range(1,N+1):
    if N % i ==0:
        factor.append(i)
    
factor.sort()

if len(factor) < K:
    print(0)
else : 
    print(factor[K-1])

