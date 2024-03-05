import sys 

read= sys.stdin.readline

# 어떤 자연수 N이 있을때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라고 한다. 

# 245의 분해합은 245 + 2 + 4+ 5 = 256 
# 따라서 245는 256의 생성자 
# 어떤 자연수의 경우 생성자가 없을수도 있고 , 반대로 생성자가 여러개일수도 있다 

N = read().rstrip()

count = 0
# 생성자 
constructor = 0

# 분해합 = N + N 각자리수 
decompositionSum = int(N)

for i in range(1,decompositionSum-1):
    n_list = list(map(int, str(i)))
    n_decompositonSum = i

    for number in n_list:
        n_decompositonSum += number

    if decompositionSum == n_decompositonSum:
        if constructor == 0:
            constructor = i
            count += 1
        else : 
            constructor = min(constructor, i)
            count +=1 
    

print(constructor)
    





