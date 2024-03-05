import sys 

read = sys.stdin.readline

T = int(read())


for _ in range(T):
    k, n = map(int, read().split())
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