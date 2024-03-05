# 세준이는 기말고사 말아먹음 
# 자기점수중 최대값을 고름 
# 이 값을 M 
# 모든 점수를  점수/M * 100 고침 

import sys

read = sys.stdin.readline

N = int(read())

scores = list(map(int, read().split()))

M = max(scores)

total = 0.0
for score in scores:
    total += float((score/M)*100)

average = total / N
print(average)