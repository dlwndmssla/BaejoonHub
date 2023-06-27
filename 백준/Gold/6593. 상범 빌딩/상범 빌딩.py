import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
#input = sys.stdin.readline
    
def bfs(graph,v):
    z,y,x = v
    queue = deque()
    queue.append(v)
    visited = [[[-1 for i in range(x1)] for j in range(y1)] for k in range(z1)]
    visited[z][y][x] = 0
    while queue:
        v = queue.popleft()
        z,y,x = v
        
        for t in range(6):
            x0 = x + [-1,1,0,0,0,0][t]
            y0 = y + [0,0,-1,1,0,0][t]
            z0 = z + [0,0,0,0,-1,1][t]
            if 0 <= x0 <= x1-1 and 0 <= y0 <= y1-1 and 0 <= z0 <= z1-1:
                if visited[z0][y0][x0] == -1:
                    if graph[z0][y0][x0] == '.' or graph[z0][y0][x0] == 'E':
                        v0 = [z0,y0,x0]
                        queue.append(v0)
                        visited[z0][y0][x0] = visited[z][y][x] + 1
                        if graph[z0][y0][x0] == 'E':
                            return visited[z0][y0][x0]
        
while True:                
    z1,y1,x1 = map(int,input().split())
    if [z1,y1,x1] == [0,0,0]: break
    graph = []
    for i in range(z1):
        zlist = []
        for j in range(y1):
            ex = list(map(str,input().rstrip()))
            zlist.append(ex)
            if 'S' in ex:
                v = [i,j,ex.index('S')] #z,y,x 순
        p = input()     
        graph.append(zlist)

    cnt =  bfs(graph,v)
    if cnt != -1 and cnt != None :    
        print("Escaped in {} minute(s).".format(cnt)) 
    else:
        print("Trapped!")