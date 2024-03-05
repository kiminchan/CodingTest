import sys 

read = sys.stdin.readline 

board = [[0 for col in range(9)] for row in range(9)]

for i in range(9):
    board[i] = list(map(int, read().split()))

max = max(map(max,board))
max_count = 0
#print(max(map(max,board)))

for i in range(9):
    for j in range(9):
        if board[i][j] == max:
            max_count +=1 
            a, b = i, j 
print(max)
print(a+1, b+1)

