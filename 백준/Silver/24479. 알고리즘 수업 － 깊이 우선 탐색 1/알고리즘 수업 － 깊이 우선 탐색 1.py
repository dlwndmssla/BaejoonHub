import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n,m,r = list(map(int,input().split()))

graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
    
    
for i in range(n):
    graph[i].sort()
    
visited = [False for i in range(n+1)]

route = [0 for i in range(n+1)]
count = 1
route[r] = count

def dfs(graph,v,visited,route):
    global count
    visited[v] = True

    for t in graph[v]:
        if not visited[t]:
            visited[t] = True
            count +=1
            route[t] = count

            dfs(graph,t,visited,route)
            
dfs(graph,r,visited,route)   
    
for j in route[1:]:
    print(j)