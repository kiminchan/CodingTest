import sys

read = sys.stdin.readline

N = int(read())

dance = {}
count = 0
for _ in range(N):
    a, b = read().split()
    if a == "ChongChong":
        dance[b] = 1
    elif b == "ChongChong":
        dance[a] = 1
    elif a in dance.keys():
        dance[b] = 1
    elif b in dance.keys():
        dance[a] = 1


print(len(dance)+1)            
    

    