from collections import deque

def dfs(graph,v,visited):
    if len(visited)>=5:
        # print(visited)
        print(1)
        exit()
    for i in graph[v]:
        if i in visited: continue
        visited.append(i)            
        dfs(graph,i,visited)
        visited.pop()     
        
a,b = map(int, input().split())
graph = {i:[] for i in range(a)}

for i in range(b):
    p,q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)
for v in range(a):
    visited = deque([v])
    dfs(graph,v,visited)
   
     
print(0)