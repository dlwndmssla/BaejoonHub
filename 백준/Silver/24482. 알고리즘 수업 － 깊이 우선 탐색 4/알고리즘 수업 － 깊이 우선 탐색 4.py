import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n,m,r = list(map(int,input().split()))

graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
    
    
for i in range(n+1):
    graph[i].sort(reverse=True)


visited = [False for i in range(n+1)]
depth = [0]+[-1 for i in range(n)]

depth[r] = 0

def dfs(v):
    visited[v] = True
    cnt = depth[v]+1
    for t in graph[v]:
        if visited[t]: continue
        visited[t] = True
        depth[t] = cnt

        dfs(t)
            
dfs(r)   
    
for j in depth[1:]:
    print(j)
    