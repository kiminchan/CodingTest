# B진법 수 N이 주어진다.
# 이수를 10진법으로 바꿔서 출력하는 프로그램 

import sys 
import string 
read = sys.stdin.readline

# 입력 
# N과 B과 주어짐 
N , B = read().split()
B = int(B)

# 반복문
# 길이는 N의 len 
length = len(N)

alphabet_list = list(string.ascii_uppercase)

N_list =list(N)
N_list.reverse()
total = 0

for i in range(length):
    if N_list[i] in alphabet_list:
        total += (((B**i)*(alphabet_list.index(N_list[i])+10)))
    else:
        total += (((B**i)*int(N_list[i])))
# 출력 
# B진법 수 N을 10진법으로 출력 
print(total)


#####################################################################

'''
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = read().split()

answer = 0 

for i, num in enumerate(n[::-1]):
    answer += int(b) ** i * num_list.index(num)
print(answer)
'''



