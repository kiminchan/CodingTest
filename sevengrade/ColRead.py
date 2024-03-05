# 장난감에 있는 글자들은 영어 대문자 'A' 부터 'Z'
# 영어 소문자 'a' 부터 'z'
# 숫자 '0' 부터 '9'이다 

# 글자들을 수평으로 일렬로 붙여서 단어를 만든다 
import sys

read = sys.stdin.readline

word_matrix = []
length = []

for i in range(5):
    word = read().strip()
    word_matrix.append(word)
    length.append(len(word))

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            print(word_matrix[j][i], end="")
