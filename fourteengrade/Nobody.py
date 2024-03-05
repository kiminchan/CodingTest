import sys

read = sys.stdin.readline

N, M = map(int,read().split())

no_ear_set = set()
no_see_set = set()
for i in range(N):
    no_ear = read().strip()
    no_ear_set.add(no_ear)
for i in range(M):
    no_see = read().rstrip()
    no_see_set.add(no_see)

print(len(no_ear_set & no_see_set))
intersection_set = list(no_ear_set & no_see_set)

intersection_set.sort()
for i in intersection_set:
    print(i)

