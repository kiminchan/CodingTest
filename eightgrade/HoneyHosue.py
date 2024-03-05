# 중앙의 방 1부터 시작해서 이웃하는 방에 들어가서
# 1씩 증가하는 번호를 주소로 매길수 있따 
# 숫자 N이 주어졌을때, 벌집의 중앙 1에서 N번 방까지 
# 최소 개수의 방을 지나서 갈때 몇 개의 방을 지나가는지
# (시작과 끝을 포함하여)를 계산하는 프로그램 
# 13 까지는 3개 58까지는 5개 
import sys 

read = sys.stdin.readline

N = int(read())

min = 1 # 벌집 개수 
room_count = 1 # 방문 횟수 
# 1 6 12 18 24 
# i=0부터 
# (6 * i) + 1  
# 위에 규칙대로 room_count가 1 증가한다 
# N = 66 그러면 최소 이동 횟수 : 6 

while N > min:
    min += 6 * room_count 
    room_count += 1

print(room_count)




