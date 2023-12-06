n = int(input())
ans = 0
for i in range(n):
    ex = list(map(int,input().split()))
    ex1 = list(set(ex))
    if len(ex1) == 1:
        ans = max(10000+1000*ex1[0],ans)
    elif len(ex1) == 3:
        ans = max(max(ex)*100,ans)
    else:
        if ex.count(ex1[0]) == 2:
            ans = max(1000+ex1[0]*100,ans)
        else:
            ans = max(1000+ex1[1]*100,ans)
            
print(ans)