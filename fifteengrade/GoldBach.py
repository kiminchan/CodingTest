# 골드바흐의 추측 
# 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있음 
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션
# 짝수 N이 주어졌을때 골드바흐의 파티션의 개수를 구하자
# 두 소수의 순서만 다른것은 같은 파티션 
import sys 

# https://portable-paper.tistory.com/entry/17103-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90-%ED%8C%8C%ED%8B%B0%EC%85%98-python
read = sys.stdin.readline 

primeNum = [False, False] + [True] * 999999

for i in range(2,1000001):
    if primeNum[i]:
        for j in range(i*2, 1000001, i):
            primeNum[j] = False

T = int(read())

for i in range(T):
    count = 0
    N = int(read())
    # 순서는 바뀌어도 똑같다 
    for j in range(2, N//2+1):
        if primeNum[j] and primeNum[N-j]:
            count += 1
    print(count)


