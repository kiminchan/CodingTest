# 1. 자주 나오는 단어일수록 앞에 배치
# 2. 해당 단어의 길이가 길수록 앞에 배치
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치

# M보다 짧은 길이의 단어의 경우 읽는 것만으로도
# 외울 수 있기 때문에 M이상인 단어들만 외운다고함 

import sys

read = sys.stdin.readline

# 영어 지문에 나오는 단어의 개수 N
# 외울 단어의 길이 기준이 되는 M 
N, M = map(int, read().split())

dict = {}
for i in range(N):
    alpabet_word = read().rstrip()

    if len(alpabet_word) < M:
        continue
    else:
        if alpabet_word in dict:
            dict[alpabet_word] +=1
        else:
            dict[alpabet_word] = 1

dict = sorted(dict.items(), key=lambda x :(-x[1], -len(x[0]), x[0]))

for i in dict:
    print(i[0])
