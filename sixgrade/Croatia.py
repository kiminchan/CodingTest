import sys

read= sys.stdin.readline

word = read().strip()

croatia_words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = len(word)

for i in croatia_words:
    if word.count(i) > 0:
        count -= word.count(i)
    
print(count)


