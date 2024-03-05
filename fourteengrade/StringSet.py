import sys 

read = sys.stdin.readline

N, M = map(int, read().split())

S = set()

for i in range(N):
    S.add(read())

words = []
for i in range(M):
    words.append(read())

count = 0
for word in words:
    if word in S:
        count += 1

print(count)


