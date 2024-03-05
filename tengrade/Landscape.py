import sys 

read = sys.stdin.readline

N = int(read())

x = [] 
y = []

for i in range(N):
    x_dot, y_dot = map(int,read().split())
    x.append(x_dot)
    y.append(y_dot)


print(abs((max(x)-min(x))* abs(max(y)- min(y))))
