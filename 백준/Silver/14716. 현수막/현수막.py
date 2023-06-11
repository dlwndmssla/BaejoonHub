import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

a,b = map(int, input().split())
graph = []
visited = set()

for i in range(a):
    ex = list(map(int, input().split()))
    graph.append(ex)
    
def dfs(graph,x,y,visited):
    node = 1000*x+y
    visited.add(node)
    for t in range(8):
        x0 = [-1,1,0,0,-1,-1,1,1][t] + x
        y0 = [0,0,-1,1,-1,1,-1,1][t] + y
        if 0 <= x0 <= b-1 and 0 <= y0 <= a-1:
            node0 = 1000*x0+y0
            if graph[y0][x0] == 1 and node0 not in visited:
                visited.add(node0) 
                dfs(graph, x0, y0,visited)
            elif node0 in visited:
                continue
            
k = 0
for y in range(a):
    for x in range(b):
        node = 1000*x+y
        if node not in visited and graph[y][x] == 1:
            dfs(graph,x,y,visited)
            k += 1
            
print(k)