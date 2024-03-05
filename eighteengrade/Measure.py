import sys 

read = sys.stdin.readline

# 양수 A가 N의 진짜 약수가 되려면 
# N이 A의 배수이고, A가 1과 N이 아니여야 한다 
# 어떤 수 N의 진짜 약수가 모두 주어 질때 
# N을 구하는 프로그램 

# N의 약수 개수 (50개보다 작거나 같은 자연수)
measure_count = int(read())

# N의 진짜 약수(2보다 크거나 같은 자연수 중복 x)
measure = list(map(int, read().split()))

print(max(measure)* min(measure))