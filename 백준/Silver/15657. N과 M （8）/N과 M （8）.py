def bk(k):
    if len(s) == m:
        print(" ".join(map(str,s)))
        return
    
    for i in range(len(num)):
        
        if len(s) !=0:
            if s[-1] > num[i]: continue
            
        s.append(num[i])
        bk(k+1)
        s.pop()

n,m = list(map(int,input().split()))

num = list(map(int,input().split()))
num.sort()

s = []

bk(0)      