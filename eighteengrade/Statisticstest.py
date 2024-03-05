import sys 

read = sys.stdin.readline

N = int(read())
number_list =[]
for i in range(N):
    number_list.append(int(read()))

number_list.sort()
# 산술평균 : N개의 수들을 N으로 나눈 값
print(round(sum(number_list)/len(number_list)))

# 중앙 값 : N개의 수들을 증가하는 순서로 나열했을 경우, 중앙에 위치하는 값
print(number_list[len(number_list)//2])
# 최빈 값 : N개의 수들을 중 가장 많이 나타내는 값
dict = {}
for num in number_list:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
mx = max(dict.values())
mx_list =[]

for key, value in dict.items():
    if mx == value:
        mx_list.append(key)
print(mx_list)
if len(mx_list) > 1:
    print(mx_list[1])
else:
    print(mx_list[0])

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(max(number_list)-min(number_list))
