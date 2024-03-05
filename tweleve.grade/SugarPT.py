import sys 

read = sys.stdin.readline

sugar = int(read())

count = 0

while sugar >= 0 :
    if sugar % 5 == 0 :
        count += sugar // 5
        break 
    sugar -= 3 
    count += 1 


print(count)