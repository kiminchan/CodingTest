import sys

read = sys.stdin.readline 

word = list(read().strip())

set_list = set()
count = 0
for i in range(0,len(word)):
    count += 1
    for j in range(0,len(word)-i):
        set_list.add(''.join(word[j:j+count]))

# set_list = set(word_list)는 word_list가 
# 원소도 리스트이므로 바로 바꿔주면 type eroor
# 원소인 리스트를 튜플로 바꾼다음 set으로 변환 
print(len(set_list))



