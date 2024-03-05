import sys 

read = sys.stdin.readline


x, y, w, h = map(int, read().split())

if abs(x-w) > abs(y-h):
    if abs(y-h) < y and abs(y-h) < x:
        print(abs(y-h))
    else:
        if x < y :
            print(x)
        else :
            print(y)

else:
    if abs(x-w) < x and abs(x-w) < y:
        print(abs(x-w))
    else:
        if x < y :
            print(x)
        else :
            print(y)
