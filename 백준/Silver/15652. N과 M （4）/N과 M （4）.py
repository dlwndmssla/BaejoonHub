def bk():
    if m == len(s):
        print(" ".join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if len(s) == 0:
            s.append(i)
        elif s[-1] <= i:
            s.append(i)
        else: continue
        
        bk()
        s.pop()

n,m = list(map(int,input().split()))

s = []

bk()