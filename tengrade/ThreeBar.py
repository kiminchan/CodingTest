# a,b,c 세막대 
import sys
read = sys.stdin.readline 

triangle = sorted(list(map(int,read().split())))

# 가장 긴변의 길이 < 두 짧은 변의 길이의 합 
if triangle[0] + triangle[1] <= triangle[2]:
    triangle[2] = triangle[0] + triangle[1] - 1
    print(sum(triangle))
else:
    print(sum(triangle))


