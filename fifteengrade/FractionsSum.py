import sys 

read = sys.stdin.readline

a, b = map(int, read().split())
c, d = map(int, read().split())

def gcd(a,b):
    r = 0
    while(b !=0):
        r = a%b
        a = b
        b = r 
    return a 

#분자 
numerator = (a*d) +(c*b)
#분모 
denominator = b*d

new_numerator = 0 
new_denominator = 0

if gcd(denominator, numerator) == 1:
    print(numerator, denominator)
else: 
    while gcd(new_denominator, new_numerator) !=1:
        new_numerator = numerator // gcd(denominator, numerator)
        new_denominator = denominator // gcd(denominator, numerator)
    print(new_numerator, new_denominator)

