import sys
read = sys.stdin.readline

N, M = map(int, read().split())
board = []
count = []

for _ in range(N):
    board.append(read().rstrip()) 

# 8 x 8 정사각형 형태로 잘라서 다시 칠해야 하는 정사각형
# 이 최소개수를 고르시오 

# 시작점이 필요함 
for x in range(N-7):
    for y in range(M-7):
        white = 0 
        black = 0 
        for i in range(x,x+8):
            for j in range(y, y+8):
                # i + j 합이 짝수일때 
                if (i+j) % 2 == 0 :
                    if board[i][j] != "W":
                        # 첫번쨰 타일이 하얀색일때 
                        # WBWBWBWB
                        # 0 2 4 6 : 짝수는 W 
                        # 1 3 5 7 : 홀수는 B  
                        white += 1 
                    if board[i][j] != "B":
                        # 첫번째 타일이 검은색일때
                        # 0 2 4 6 : 짝수는 B 
                        # 1 3 5 7 : 홀수는 W 
                        # BWBWBWBW 
                        black += 1
                else :
                    if board[i][j] != "B":
                        white +=1 
                    if board[i][j] != "W":
                        black +=1 
        count.append(min(black,white))

print(min(count))



