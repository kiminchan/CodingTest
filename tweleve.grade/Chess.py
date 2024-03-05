import sys 

read = sys.stdin.readline
N, M = map(int,read().split())
board = []
result =[]
for i in range(N):
    board.append(read())

# 체스판에서 시작점을 잡기위한 반복문 
for a in range(N-7):
    for b in range(M-7):
        # 시작하는 타일의 색깔 구분 
        white = 0
        black = 0 
        for i in range(a, a+8):
            for j in range(b, b+8):
                # (i + j) 합이 짝수일때, W가 아니라면 white +=1 
                # 홀수일때, B가 아니라면 black +=1 
                if (i+j) % 2 == 0:
                    if board [i][j] != 'W':
                        white += 1 
                    if board[i][j] != 'B':
                        black += 1
                else:
                    if board[i][j] != 'B':
                        white +=1 
                    if board[i][j] != 'W':
                        black +=1 
        # white, black 중 작은수를 result에 넣는다 
        result.append(min(white, black))

print(min(result))

