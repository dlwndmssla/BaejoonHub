import sys
input=sys.stdin.readline

a,b = list(map(int, input().split()))
c,d = list(map(int, input().split()))

ans = []
for i in range(4):
    ans.append(a/c+b/d)
    a,b,c,d = c,a,d,b
    
print(ans.index(max(ans)))