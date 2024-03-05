import sys

read = sys.stdin.readline

# 이항계수 : 주어진 집합에서 원하는개수 만큼 순서없이 뽑는 조합의 수를 의미 
n, k = map(int, read().split())

# n!
numerator = 1 
for i in range(1,n+1):
    numerator *= i 

# (n-k)! x k!
denominator = 1 
a = 1 
b = 1 
for i in range(1,(n-k)+1):
    a *= i 

for i in range(1,k+1):
    b *= i 

denominator = a * b 
print(numerator//denominator)

