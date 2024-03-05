import sys
read = sys.stdin.readline

T = int(read()) 

Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

for i in range(T):
    Quarter_count = 0
    Dime_count = 0
    Nickel_count = 0
    Penny_count = 0
    C = int(read())
    while(True):
        if C == 0:
            break
        if C >= Quarter:
            Quarter_count += C / Quarter
            C = C % Quarter
        elif C < Quarter and C >= Dime:
            Dime_count += C / Dime
            C = C % Dime 
        elif C < Dime and C >= Nickel:
            Nickel_count += C /Nickel
            C = C % Nickel
        else:
            Penny_count += C/Penny
            C = C % Penny
    print(int(Quarter_count), int(Dime_count),int(Nickel_count), int(Penny_count))





