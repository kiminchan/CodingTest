import sys
read = sys.stdin.readline

N = int(read())

list =[] 
for i in range(N):
    list.append(int(read()))

list.sort()

# 산술 평균 : N개의 수들의 합을 N으로 나눈 값 
print(round(sum(list)/len(list)))

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값 
print(list[len(list)//2])

# 최빈값 : N개의 수들중 가장 많이 나타나는 값 여러 개 있을 때는 두번째로 작은 값을 출력 
dic = dict()
for i in list:
    if i in dic :
        dic[i] += 1
    else:
        dic[i] = 1
    
mx = max(dic.values())
mx_dic =[] 

for i in dic:
    if mx == dic[i]:
        mx_dic.append(i)

if len(mx_dic)> 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이 
print(max(list)-min(list))