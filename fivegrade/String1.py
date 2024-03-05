import sys

read = sys.stdin.readline

T = int(read())

for i in range(T):
    word = read().strip()
    print(word[0]+word[-1])