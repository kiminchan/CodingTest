import sys

read = sys.stdin.readline

N, k = map(int, read().split())

scores = list(map(int,read().split()))

scores.sort()
scores.reverse()

print(scores[k-1])
