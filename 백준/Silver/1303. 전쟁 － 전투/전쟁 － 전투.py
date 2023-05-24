import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n,m = map(int, input().split())
battle = []
for i in range(m):
    ex = list(map(str,input().rstrip()))
    battle.append(ex)

visited = [[False for i in range(n)] for j in range(m)]
x,y = 0,0
count0 = 0
def dfs(graph, x, y, visited):
    visited[y][x] = True
    for k in range(4):
        i = [0,0,-1,1][k]
        j = [-1,1,0,0][k]
        if 0 <=x+i<= n-1 and 0 <=y+j<= m-1 and not visited[y+j][x+i] and battle[y][x] == battle[y+j][x+i]:
            visited[y+j][x+i] = True
            dfs(graph,x+i,y+j,visited)
                    
wc,bc = 0,0
count0 = 0
graph = battle
for s in range(n):
    for t in range(m):
        x,y = s,t
        if visited[y][x] == True:
            continue
        dfs(graph, x, y, visited)
        count_ex = sum([sum(visited[kk]) for kk in range(len(visited))])
        
        if battle[y][x] == 'W':
            wc += pow(count_ex- count0,2)
        else:
            bc += pow(count_ex- count0,2)
        count0 = count_ex    
        
print(wc, bc)