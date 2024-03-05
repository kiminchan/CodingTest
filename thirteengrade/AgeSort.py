import sys

read= sys.stdin.readline

n = int(read())

person =[]
for _ in range(n):
    age, name = read().split()
    person.append([int(age),name])

person.sort(key=lambda x:(x[0]))

for i in range (n):
    print(person[i][0], person[i][1])




    

