# 종말의 수란 어떤 수에 6이 적어도 3개이상 연속으로 들어가는수 

# 제일 작은 종말의 수는 666 

# 1666, 2666, 3666, .... 

import sys 

read = sys.stdin.readline

N = int(read())
nth = 666
count = 0 
while True:
    if '666' in str(nth):
        count += 1
     
    if count == N:
        print(nth)
        break
    nth +=1 
