import sys

read = sys.stdin.readline

n =int(read())
word_list =[]
for i in range(n):
    word= read().strip()
    if word not in word_list:
        word_list.append(word)

word_list.sort(key=lambda x:(len(x), x))

for word in word_list:
    print(word)
