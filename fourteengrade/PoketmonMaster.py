import sys 

read = sys.stdin.readline

# N : 도감에 수록되어있는 포켓몬의 개수 
# M : 맞춰야 하는 문제의 개수 
N, M = map(int, read().split())
dict = {}
for i in range(1,N+1):
    pocketmon_name = read().strip()
    dict[pocketmon_name] = i
    dict[i] = pocketmon_name


for i in range(M):
    problem = read().strip()
    # 문자열이 숫자로만 이루어져 있는지 아닌지 확인 
    if problem.isdigit():
        print(dict[int(problem)])
    else:
        print(dict[problem])
       
