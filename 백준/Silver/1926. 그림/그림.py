import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

a,b = map(int, input().split())
graph = []
for i in range(a):
    ex = list(map(int, input().split()))
    graph.append(ex)
    

def dfs(graph,x,y,visited):
    node = 1000*x+y
    visited.add(node)
    for t in range(4):
        x0 = [-1,1,0,0][t] + x
        y0 = [0,0,-1,1][t] + y
        if 0 <= x0 <= b-1 and 0 <= y0 <= a-1:
            node0 = 1000*x0+y0
            if graph[y0][x0] == 1 and node0 not in visited :
                visited.add(node0)
                dfs(graph, x0, y0,visited)
            elif node0 in visited:
                continue

c0 = 0
k = 0
num = 0

visited = set()

for y in range(a):
    for x in range(b):
        node = 1000*x+y
        if node not in visited and graph[y][x] == 1:
            dfs(graph,x,y,visited)
            c1 = len(visited)
            k = max(k, c1-c0)
            c0 = c1
            num += 1
            
print(num)
print(k)  
         