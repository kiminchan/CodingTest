# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 
# 금속 핀이 있는곳까지 시계방향으로 돌려야한다 

# 숫자 1을 걸려면 총 2초
# 1보다 큰수를 거는데 걸리는시간은 이보다 더 걸리며 
# 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸림 

# 상근이의 할머니는 전화번호를 각 숫자에 해당하는 문자로 외운다 
# 어떤 단어를 걸때, 각 알파벳에 해당하는 숫자를 걸면 된다.

# UNUCIC 868242 같다 

# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 최소시간을
# 구하는 프로그램을 작성하시오 
import sys 

# 입력 
# 알파벳 대문자 문자열 
read = sys.stdin.readline
alphabet = read().strip().upper()

time = 0

dial_word = {'ABC' : 3, 'DEF' : 4 ,'GHI' : 5, 'JKL' : 6, 'MNO' : 7, 'PQRS' : 8 , 'TUV' : 9 , 'WXYZ': 10}

for char in alphabet:
    for key in dial_word:
        if char in key:
            time += dial_word[key]

# 출력 
# 전화를 걸기 위해 걸리는 최소 시간 
print(time)




