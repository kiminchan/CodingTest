import sys

read = sys.stdin.readline

while True:
    a,b = map(int,read().split())
    if a == 0 and b == 0 :
        break
    
    # 출력 
    # 첫번째 수가 두번째 숫자의 약수 : factor
    # 배수 : multiple 
    # 둘다 아니면 : neither

    # 배수 약수 정의가 뭘까?
    if b%a == 0:
        print("factor")
    elif a%b == 0:
        print("multiple")
    else:
        print("neither")