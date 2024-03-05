import sys

read = sys.stdin.readline
word = read().strip()

i = int(read())

word_list = [char for char in word]

print(word_list[i-1])
