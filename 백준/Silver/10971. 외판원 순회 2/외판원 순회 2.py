import sys
input = sys.stdin.readline

def bk(m):
    global ans
    if len(s) == n:
        s0 = s+[s[0]]
        dist = [ city[s0[i]][s0[i+1]] for i in range(n)]
        if 0 not in dist:
            ans = min(ans,sum(dist))
        return
    
    for i in range(n):
        if visited[i]: continue
        if len(s) != 0 and city[s[-1]][i] == 0: continue
        visited[i] = True
        s.append(i)
        bk(m+1)
        s.pop()
        visited[i] = False


n = int(input())
city = [list(map(int,input().split())) for i in range(n)]


ans = 10e7
s = []
visited = [False for i in range(n)]

bk(0)
print(int(ans))
