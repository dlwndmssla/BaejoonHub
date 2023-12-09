ans = 0
ans0 = 0
for i in range(4):
    a,b = map(int,input().split())
    ans0 += (b-a)
    ans0 = min(ans0,10000)
    ans = max(ans,ans0)
    
print(ans)