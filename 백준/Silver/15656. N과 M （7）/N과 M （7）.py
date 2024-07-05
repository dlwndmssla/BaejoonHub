
def bk(k):
    if m == len(s):
        print(" ".join(map(str,s)))
        return
    
    for i in range(len(num)):
        
        s.append(num[i])
        bk(k+1)
        s.pop()

n,m = list(map(int,input().split()))
num = list(map(int,input().split()))
num.sort()
s = []
        
bk(0)      