import sys 

# 입력 값이 그대로 들어오면 그대로 출력
# 아니라면 EOF(End of File)상태라면 break 걸어줌 
# https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-11718-%EA%B7%B8%EB%8C%80%EB%A1%9C-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
read = sys.stdin.readline
for _ in range(100):
    try:
        print(read().strip())
    except EOFError:
        break