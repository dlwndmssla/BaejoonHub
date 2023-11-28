import sys
input = sys.stdin.readline

n = int(input())
ans = [0]*1001

ans[1] = 1
ans[2] = 1
ans[3]= 2 

for i in range(4,1001):
    ans[i] = (sum(ans[:i-1])+1)

print(ans[n])