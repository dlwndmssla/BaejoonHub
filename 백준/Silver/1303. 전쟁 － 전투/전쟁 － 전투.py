import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(graph, x, y, visited):
    visited[y][x] = True
    for k in range(4):
        y0,x0= y+dy[k],x+dx[k]
        if not (0 <=x0<= n-1 and 0 <=y0<= m-1): continue
        if visited[y0][x0]: continue
        if battle[y][x] != battle[y0][x0]: continue
        visited[y0][x0] = True
        dfs(graph,x0,y0,visited)
        
        
n,m = map(int, input().split())
battle = [list(map(str,input().rstrip())) for i in range(m)]
visited = [[False for i in range(n)] for j in range(m)]
wc,bc,cnt = 0,0,0

for x in range(n):
    for y in range(m):
        if visited[y][x] == True: continue
        dfs(battle, x, y, visited)
        count_ex = sum([sum(visited[kk]) for kk in range(len(visited))])
        if battle[y][x] == 'W':
            wc += pow(count_ex- cnt,2)
        else:
            bc += pow(count_ex- cnt,2)
        cnt = count_ex    

print(wc, bc)