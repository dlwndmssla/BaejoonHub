import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

r,c = map(int, input().split())
graph = []
for i in range(r):
    ex = list(map(str, input().rstrip()))
    graph.append(ex)

def dfs(graph,x,y,visited,vs):
    node = 1000*x+y
    visited.add(node)
    for t in range(4):
        x0 = [-1,1,0,0][t] + x
        y0 = [0,0,-1,1][t] + y
        if 0 <= x0 <= c-1 and 0 <= y0 <= r-1:
            node0 = 1000*x0+y0
            if graph[y0][x0] != '#' and node0 not in visited:
                visited.add(node0)
                vs.append(graph[y0][x0])    
                dfs(graph, x0, y0,visited,vs)
            elif node0 in visited:
                continue
            
visited = set()
o0, v0 = 0, 0
k = 0
for y in range(r):
    for x in range(c):
        o1, v1 = 0, 0
        vs = []
        node = 1000*x+y
        if graph[y][x] != '#' and node not in visited:
            vs.append(graph[y][x])   
            dfs(graph,x,y,visited,vs)
            k += 1
            o1, v1 = vs.count('o'),vs.count('v')
            if v1 >= o1:
                v0 += v1
            else:
                o0 += o1

print(o0, v0)