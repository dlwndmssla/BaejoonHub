n,k = list(map(int,input().split()))

cnt = [ int(input()) for i in range(n)][::-1]
# print(cnt)
ans = 0
for i in range(n):
    ans += int(k/cnt[i])
    k = k%cnt[i]
    
print(ans)
