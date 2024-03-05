# ax + by = c
# dx + ey = f
# -999 <= a, b, c, d, e, f <= 999
# x,y는 -999 ~ 999이 입력되는것이 보장됨 
import sys 

read = sys.stdin.readline

a, b, c, d, e, f = map(int,read().split())


# (x,y를 만족시키는 해가 유일하게 존재) => 해가 무조건 1개 있다.
for x in range(-999,1000):
    for y in range(-999, 1000):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
            print(x, y)
            break
