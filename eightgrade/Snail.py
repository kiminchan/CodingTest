import sys 
read = sys.stdin.readline

A, B ,V = map(int,read().split())

# 올라가야할 거리 V-B   
# 달팽이가 하루에 갈수 있는거리 (A-B) 

# (V-B)%(A-B)== 0 이면 낮동안에 정상에 갔다는 소리 
if (V-B)%(A-B)==0:
    print((V-B)//(A-B))
# (V-B)%(A-B)=! 0 이면 낮동안에 정상에 가지 못해 밤에 미끄러짐
if (V-B)%(A-B)!= 0:
    print((V-B)//(A-B)+1)


'''
import sys  
import math 
A, B, V = map(int,sys.stdin.readline().split())

count_day = (V-B) / (A-B)
print(math.ceil(count_day))
'''