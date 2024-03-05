# 도현이는 총 N개의 바구니 
# 각각의 바구니에는 1~ N번 번호가 순서대로 
# M번 바구니를 역순으로 만들려고 한다
# 순서를 역순으로 만들 범위를 정하고, 그 범위에 들어있는
# 바구니의 순서를 역순을 만듦 
# 바구니의 순서를 어떻게 바꿀지 주어졌을때, 순서를 역순으로 만든 다음
# 바구니에 적혀있는 번호를 가장 왼쪽부터 출력 

import sys
read = sys.stdin.readline() 
# 입력 
# N (1<= N <= 100)
N, M = map(int, read.split())
# M (1<= M <= 100)
basket =[i for i in range(1,N+1)]

for _ in range(M):
    read = sys.stdin.readline()
    i,j = map(int, read.split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for idx in basket:
    print(idx , end=" ")
        

