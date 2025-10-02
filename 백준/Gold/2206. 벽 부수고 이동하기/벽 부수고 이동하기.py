from collections import deque
n,m = list(map(int,input().split()))
grid = {(i,j) for i in range(n) for j,v in enumerate(map(int,input())) if v}
visited = {(0,0):[1,1,0,0]} #(y,x):(not broken,broken)
queue = deque([(0,0)])
dirs = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
while queue:
    y,x = queue.popleft()
    v = visited[(y,x)]
    for (dy,dx) in dirs.values():
        k = (y+dy,x+dx)
        a = int(k in grid)
        if not (0 <= k[0] <= n-1) or not (0 <= k[1] <= m-1): continue
        nv = visited.get(k,[n*m,n*m,a,a])
        w0,w = v[3],nv[3]
        if (w0,w) == (1,1): continue

        
        c1 = (not w and nv[0]>v[0]+1)
        c2 = ((w0,w) == (0,1) and nv[1]>v[0]+1)
        c3 = ((w0,w) == (1,0) and nv[1]>v[1]+1)
        c4 = ((v[2],nv[2]) == (1,0) and nv[1]>v[1]+1)

        if not (c1 or c2 or c3 or c4): continue
        if c1: nv[0] = v[0]+1
        if c2: nv[1],nv[2] =v[0]+1,1
        if c3 or c4: nv[1],nv[2] =v[1]+1,1
        visited[k] = nv
        queue.append(k)               

print(min(visited.get((n-1,m-1),(-1,-1,-1))[0:2]))
