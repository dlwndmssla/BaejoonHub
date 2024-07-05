def bk(m,total):
    global cnt

    if m >= n:
        return
    
    total += num[m]
    if total == s: cnt +=1 

    bk(m+1,total)
    bk(m+1,total-num[m])

n,s = list(map(int,input().split()))
num = list(map(int,input().split()))

cnt = 0
bk(0,0)

print(cnt)