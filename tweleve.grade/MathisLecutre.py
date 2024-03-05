import sys 

read = sys.stdin.readline

a, b, c, d, e, f = map(int, read().split())

# 문제에 조건을 잘 보고 해를 구하는 것이니 해를 찾게 한다.
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
            print(i, j)

