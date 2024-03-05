import sys 

read = sys.stdin.readline

N, B = map(int,read().split())

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num_list = list(num)
change_num = 0 

str = ""
while(True):
    if N/B == 0:
        # 먼저 나온게 제일 끝자리로 나중에 나온게 제일 처음 자리로 
        # 그래서 reverse()로 출력 
        print(str[::-1])
        break
    change_num = int(N % B)
    str += num_list[change_num]
    N = int(N/B)

    
