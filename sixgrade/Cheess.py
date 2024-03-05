# 검정색 피스는 개수가 올바름

# 흰색 피스는 개수가 올바르지 않음 

# 체스는 총 16피스 사용 
# 킹 1, 퀸 1, 룩 2, 비숍 2 , 나이트 2 , 폰 8 

# 동혁이가 발견한 흰색 피스의 개수가 주어졌을때 
# 몇개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램

import sys 

read = sys.stdin.readline

chess = [1,1,2,2,2,8]

# 입력 
# 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰 개수 
white_chess = list(map(int, read().split()))

addMinus_chess = []
# 출력 
# 첫째 줄 입력에서 주어진 순서대로 몇 개의 피스를 더하거나
# 빼야 되는지를 출력 
# 만약 수가 양수라면 그 개수만큼 더하고 음수라면 제거 

for i in range(len(chess)):
    addMinus_chess.append(chess[i]- white_chess[i])

for chess in addMinus_chess:
    print(chess, end=" ")