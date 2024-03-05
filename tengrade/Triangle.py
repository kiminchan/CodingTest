import sys

read = sys.stdin.readline

total_angle = 0
triangle = []
for i in range(3):
    triangle.append(int(read()))
    total_angle += triangle[i]


if triangle[0] == 60 and triangle[1] == 60 and triangle[2] == 60:
    print("Equilateral")

elif total_angle == 180 and (triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[0] == triangle[2]) :
    print("Isosceles")

elif total_angle == 180 and triangle[0] != triangle[1] and triangle[1] != triangle[2] and triangle[0] != triangle[2]:
    print("Scalene")

elif total_angle != 180:
    print("Error")

