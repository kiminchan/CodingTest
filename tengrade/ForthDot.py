import sys

read = sys.stdin.readline

x = []
y = []

for i in range(3):
    x_dot, y_dot = map(int,read().split())
    x.append(x_dot)
    y.append(y_dot)

four_x = 0
four_y = 0 
for x_dot in x:
    if x.count(x_dot) == 1:
        four_x += x_dot

for y_dot in y:
    if y.count(y_dot) == 1:
        four_y += y_dot

print(four_x, four_y)