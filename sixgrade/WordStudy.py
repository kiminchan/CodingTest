# 알파벳 대소문자가 주어지면 이 단어에서 가장 
# 많이 사용된 알파벳이 무엇인지 알아내는 프로그램

# 단 대소문자는 구분하지 않는다
import sys 

read = sys.stdin.readline
# 입력 
# 알파벳 대소문자로 이루어진 단어 
word = read().strip().upper()

word_list = list(set(word))

cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

# 출력
# 가장 많이 사용된 알파벳을 대문자로 출력
# 최댓값의 개수 확인 
# 1보다 크면 최댓값이 중복이라는 증거 
if cnt.count(max(cnt)) > 1 :
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])



# 가장 많이 사용된 알파벳이 여러개 존재하는 경우 
# ? 출력 