# 상근이는 사탕가게에서 설탕을 정확하게 N킬로그램 배달 
# 봉지는 3kg, 5kg 있다. 
# 상근이는 귀찮기 때문에 최대한 적은 봉지를 들고간다 
# 18kg 설탕 배달 3kg 6개해도 되지만 , 5킬로 그램 3개와 3킬로 1
# 정확하게 N kg 을 만들수 없다면 -1 
import sys
read = sys.stdin.readline

N = int(read())
bag = 0

while N >= 0:
    if N % 5 == 0:
        bag += N // 5
        print(bag)
        break
    N -= 3 
    bag += 1 
else : 
    print(-1)



