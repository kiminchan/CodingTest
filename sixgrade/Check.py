# 알파벳 소문자로만 이루어진 단어가 주어짐 

# 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램

# 팰린드롬이란 앞으로 읽을때 거꾸로 읽을때 

# 똑같은 단어 

import sys 

read = sys.stdin.readline

# 압력 
# 단어
word = read().strip()

word_list = list(word)

word_list.reverse()
word1 = ''.join(word_list)
# 출력 
# 1이면 팰린드롬 , 0이면 팰린드롬 x 
if word == word1:
    print(1)
else: 
    print(0)