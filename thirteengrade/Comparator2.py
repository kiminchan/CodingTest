import sys

read= sys.stdin.readline

n = int(read())
location =[]
for _ in range(n):
    x, y = map(int,read().split())
    location.append([x,y])


location.sort(key=lambda x:(x[1], x[0]))

for i in range(len(location)):
    print(location[i][0], location[i][1])