import sys

read = sys.stdin.readline

# 입력 : 색종이의 수 
N = int(read())

board_arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, read().split())
    # x : x ~ 10
    # y : y ~ 10 
    for i in range(y, y+10):
        for j in range(x, x + 10):
                board_arr[i][j] = 1


counts = 0     
for row in board_arr:
    counts += row.count(1)

print(counts)
        


