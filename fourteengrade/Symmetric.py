import sys 

read = sys.stdin.readline

N, M = map(int, read().split())

A_set = set((map(int,read().split())))
B_set = set((map(int,read().split())))

print(len(A_set-B_set) + len(B_set-A_set))
    
