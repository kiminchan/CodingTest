# 문자열 S를 입력받은 후 , 각 문자를 R 번 반복해 
# 새 문자열 P를 만듦

# 첫번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로
# P를 만들면 된다 
# S 에는 QR Code "alphanumeric"문자만 있음

# QR Code 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:

import sys 

read = sys.stdin.readline

T = int(read())

for _ in range(T):
    R,S = read().split()
    R = int(R)
    
    repeat_words = [char for char in S]

    repeat_word = ""

    for char in S:
        repeat_word += char * R

    print(repeat_word)
    
    
    
        




