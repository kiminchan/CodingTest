# 정사각형 이루는 점 4개 
# 과정 
# 1. 정사각형의 각 변의 중앙에 점 하나 추가
# 2. 정사각형의 중심에 점을 하나 추가 
# 초기 상태에서 위와 같은 과정을 거치면 총 4개의 정사각형이
# 생김 

import sys 
read = sys.stdin.readline

N = int(read())

dot_count = (2**N + 1)


print(dot_count**2)

# 81- 25 = 56 
