import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
ex = list(map(int, input().split()))
x = int(input())

graph = [[] for i in range(n)]
visited = [False for i in range(n)]

for i in range(n):
    if ex[i] != -1:
        graph[i].append(ex[i])
        graph[ex[i]].append(i)
    else:
        v = i

for i in range(n):
    if x in graph[i]:
        graph[i].remove(x)

graph[x] = [ex[x]]
leaf = []

def dfs(graph,v,visited,leaf):
    visited[v] = True
    if graph[v] == [x]:
        leaf.append(v)
    elif graph[v] == []:
        leaf.append(v)
    for i in graph[v]:
        if not visited[i] and i != x and v != x:
            visited[i] = True
            if len(graph[i]) == 1:
                leaf.append(i)
            dfs(graph,i,visited,leaf)

dfs(graph,v,visited,leaf)
leaf = set(leaf)
print(len(leaf))