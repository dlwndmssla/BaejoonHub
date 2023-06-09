# 10026번 #적록색맹 

#1번풀이 : 그래프를 수정함. R와 G가 같다고 다시한번 그래프를 수정해줌
#2번풀이 : 그래프는 그대로 두고 원래라면 RGB가 모두 각각의 그룹을 가지겠지만 R과 G는 서로 같은 그룹으로 처리하여 이동할수 있도록 하는 풀이 

#1번 
import sys
sys.setrecursionlimit(10 ** 6)
#input = sys.stdin.readline
n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(str, input().rstrip())))
    
graph_rg = [[0 for i in range(n)] for i in range(n)]
for o in range(n):
    for p in range(n):
        if graph[o][p] == 'R' or graph[o][p] == 'G':
            graph_rg[o][p] = 'R'
        else:
            graph_rg[o][p] = 'B'

def dfs(graph,x,y,visited):
    visited[y][x] == True
    for h in range(4):
        x0 = x + [-1,1,0,0][h]
        y0 = y + [0,0,-1,1][h]
        if 0<= x0 <= n-1 and 0<= y0 <=n-1:
            if graph[y][x] == graph[y0][x0] and not visited[y0][x0]:
                visited[y0][x0] = True
                dfs(graph,x0,y0,visited)
              
c1,c2 = 0,0
visited = [[False for i in range(n)] for j in range(n)]
for s in range(n):
    for t in range(n):
        x,y = s,t
        if not visited[y][x]:
            dfs(graph,x,y,visited)
            c1 += 1
            
visited = [[False for i in range(n)] for j in range(n)]
for s in range(n):
    for t in range(n):
        x,y = s,t
        if not visited[y][x]:
            graph = graph_rg
            dfs(graph,x,y,visited)
            c2 += 1
            
print(c1,c2)