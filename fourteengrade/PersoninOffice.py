import sys

read = sys.stdin.readline

# 출입 기록의 수 
n = int(read())
peoples = set()

for i in range(n):
    name, status = read().split()
    if status == "enter":
        peoples.add(name)
    else:
        peoples.discard(name)

peoples_list = list(peoples)

peoples_list.sort(reverse=True)

for people in peoples_list:
    print(people)




