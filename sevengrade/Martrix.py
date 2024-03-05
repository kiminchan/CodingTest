# N * M 의 크기의 두 행렬 A와 B가 주어졌을때, 
# 두 행렬을 더하는 프로그램 

import sys 

read = sys.stdin.readline
# 입력 
# 행렬 크기인 N과 M이 주어진다 
N, M = map(int,read().split())

# column : 열 (세로줄) 
# row : 행 (가로줄)
# N x M : N열 M행 
N_matrix = [[0 for col in range(M)] for row in range(N)]
M_matrix = [[0 for col in range(M)] for row in range(N)]

plus_matrix = [[] for row in range(N)]


for i in range(N):
    N_matrix[i] = list(map(int,read().split()))
for i in range(N):
    M_matrix[i] = list(map(int,read().split()))

for i in range(N):
    for j in range(M):
        plus_matrix[i].append(N_matrix[i][j]+M_matrix[i][j])

for i in range(N):
       for j in range(M):
           print(plus_matrix[i][j], end=" ")
       print("")