import sys

read = sys.stdin.readline

n = int(read())
location =[]

for _ in range(n):
    x, y = map(int,read().split())
    location.append([x,y])
location.sort()
#location.sort(key=lambda coord:(coord[0], coord[1]))

for i in range(n):
    print(location[i][0], location[i][1])
