import sys

read = sys.stdin.readline

N = int(read())

line = list(map(int, read().split()))
stack = []
count = 1
while line:
    if line[0] == count:
        line.pop(0) 
        count += 1
    else:
        stack.append(line.pop(0))
    
    while stack: 
        if stack[-1]== count:
            stack.pop()
            count +=1 
        else:
            break

if not stack:
    print("Nice")
else:
    print("Sad")

 
'''
stack =[]
snack = []

sort_line = sorted(line)

sort_num = 0


while True:
    if len(line) != 0:
        for i in range(len(line)):
            if sort_line[sort_num] == line[i]:
                snack.append(line[i])
                del line[i]
                sort_num += 1
                break
            else:
                stack.append(line[i])
                del line[i]
                break
    else:
        for i in range(len(stack)):
            if sort_line[sort_num] == stack[-1]:
                snack.append(stack[-1])
                stack.pop()
                sort_num +=1
            else:
                break
    
    if sort_num == N:
        break

if len(snack) == N:
    print("Nice")
else:
    print("Sad")
'''


            



