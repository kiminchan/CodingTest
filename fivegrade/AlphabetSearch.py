# 알파벳 소문자로만 이루어진 단어 S 주어짐 
# 각각의 알파벳에 대해, 단어에 포함되어 있는 경우 
# 처음 등장하는 위치를, 포함되어 있지 않은 경우에는
# -1을 출력하는 프로그램 

import sys
import string
# 입력 
# 단어 S 
read = sys.stdin.readline

word = read().strip()
word_list = [char for char in word]

alphabet_list = list(string.ascii_lowercase)

alphabet_search = [-1] * len(alphabet_list)

# 출력 
# a ~ z까지 단어의 첫번째 글자
for i in range(len(word_list)):
    for j in range(len(alphabet_list)):
        if word_list[i] == alphabet_list[j] and alphabet_search[j] == -1:
            alphabet_search[j] = i

for alphabet in alphabet_search:
    print(alphabet, end=" ")