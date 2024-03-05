# 그룹 단어
# 존재하는 모든 문자에 대해, 각 문자가 연속해서 나타나는 경우
# ex)
# ccazzzzbb c,a,z,b 모두 연속해서 나타나고 
# kin 도 연속해서 나타나기 때문에 그룹단어 
# aabbbccb는 떨어져서 나타나서 그룹 단어 x

# 단어 N개를 입력받아 그룹 단어의 개수를 출력

N = int(input())

group_count = 0 

for i in range(N):
    word = input()
    error = 0 
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            newword = word[j+1:]
            if newword.count(word[j]) > 0 :
                error +=1 
    if error == 0:
        group_count += 1 

print(group_count) 