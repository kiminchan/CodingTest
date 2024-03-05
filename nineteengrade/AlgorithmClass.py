import sys 
read = sys.stdin.readline


def merge_sort(A,p,r):
    if p < r :
        q = (p+r) // 2 # q는 p,r의 중간지점
        merge_sort(A,p,q) # 전반부 정렬
        merge_sort(A, q+1 , r) # 후반부 정렬 
        merge(A, p, q, r)

def merge(A,p,q,r):
    global cnt , res 
    i = p
    j = q+1
    tmp =[]

    while i<=q and j<=r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i +=1 
        else:
            tmp.append(A[j])
            j +=1 
    
    while i <= q: # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        i +=1 
    while j <= r: # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])
        j +=1 
    
    i = p 
    t = 0

    while i <=r:
        A[i] = tmp[t]
        cnt +=1 
        if cnt == K:
            res = A[i]
            break
        i += 1
        t += 1



# 배열 A의 크기와 저장 횟수 K 
N, K = map(int, read().split())

# 서로 다른 배열의 원소 
A = list(map(int, read().split()))

# 배열 A에 K번째 저장되는 수를 출력 
# 저장 횟수가 K보다 작으면 -1을 출력 

cnt = 0
res = -1
merge_sort(A, 0, N, -1)
print(res)