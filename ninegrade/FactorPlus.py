# 완전 수 : 어떤 숫자 n이 자신을 제외한 모든 약수들의 합
# 들과 같다 
# n이 완전수인지 아닌지 판단해주는 프로그램

import sys 

read = sys.stdin.readline



while True:
    n = int(read())
    factor =[]
    perfect_num = 0
    
    if n == -1:
        break
    
    for i in range(1,n+1):
        if n%i == 0:
            factor.append(i)

    factor.sort()

    for i in range(0,len(factor)-1):
        perfect_num += factor[i]
    
    if perfect_num == factor[-1]:
        print(n, "= " , end="")
        for i in range(0,len(factor)-1):
            if i == len(factor)-2:
                print(factor[i], end="\n")
            else:
                print(factor[i], "+ ",end="")
        
    else:
        print(n, "is NOT perfect.", end="\n")

    

            

    


    
