import sys

read = sys.stdin.readline


while True:
    triangle =[]
    a, b, c = map(int, read().split())
    triangle.append(a)
    triangle.append(b)
    triangle.append(c)

    triangle.sort()
    if a == 0 and b == 0 and c == 0:
        break
    if triangle[0] + triangle[1] <= triangle[2]:
        print("Invalid")
    else:
        if a == b and b == c and a == c:
            print("Equilateral")
        elif  a == b or b == c or a==c :
            print("Isosceles")
        elif a != b and b!=c and a != c:
            print("Scalene") 