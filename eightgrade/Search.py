import sys 

read = sys.stdin.readline
X  = int(read())
line =1 
# [1] , [1/2, 2/1], [3/1, 2/2, 1/3], [1/4,2/3, 3/2, 4/1]
# 짝수와 홀수의 규칙 

while X > line:
    X -= line
    line +=1 

if line%2 ==0 :
    a = X 
    b = line-X +1 
else:
    a = line-X+1
    b = X

print(a, "/", b , sep='')