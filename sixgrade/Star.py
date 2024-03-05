import sys 

read= sys.stdin.readline

n = int(read())

for i in range(1, n):
    print(" "*(n-i) + "*"*((2*i)-1))
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*((2*i)-1))



'''
for i in range(1,N+1):
    if i < 5: 
        for j in range(5-i):
            print(" ", end=" ")
        for k in range((i*2)-1):
            print("*", end=" ")
        for l in rang3e(5-i):
            print(" ", end=" ")
        print("")
    elif i == 5 :
        for i in range((i*2)-1):
            print("*" , end=" ")
        print("")
    elif i > 5 :
        for j in range(i-5):
            print(" ", end =" ")
        for k in range(((i-2*(i-5))*2)-1):
            print("*", end=" ")
        for l in range(i-5):
            print(" ", end=" ")
        print("")
'''


    

    

