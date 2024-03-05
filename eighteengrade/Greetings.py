import sys 

read = sys.stdin.readline

# 채팅 방 기록수를 나타내는 N
N = int(read())

chat = {}
count = 0
for _ in range(N):
    str = read().strip()
    if str == 'ENTER':
        for value in chat.values():
            if value == 1:
                count +=1 
        chat ={}
    else:
        if str not in chat.keys():
            chat[str] = 1
    
for value in chat.values():
    if value == 1:
        count += 1
print(count)