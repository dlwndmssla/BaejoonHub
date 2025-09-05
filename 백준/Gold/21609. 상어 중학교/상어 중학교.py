def bfs(node,b,visited):
    v = deque([node])
    c_visited = set([node])
    while v:
        y,x = v.popleft()
        for dy,dx in dir:
            y0,x0 = y+dy,x+dx
            if not (grid.get((y0,x0),-2) in [0,b]): continue
            if (y0,x0) in c_visited: continue
            v.append((y0,x0))
            c_visited.add((y0,x0))
            if grid.get((y0,x0),-2) == b : visited.add((y0,x0))

    return c_visited,visited



def do_play(grid):
    level_max,level_group,visited = 0,set(),set()
    level_key,lrb = (-1,-1),-1
    for node in [(i,j) for i in range(n) for j in range(n)]:
        b = grid.get(node,-2)

        if (node in visited) or (b <= 0): continue
        c_visited,visited = bfs(node,b,visited)

        if len(c_visited) < max(2,level_max): continue
        (ky,kx),rb = (n,n),0

        for (y,x) in c_visited:
            if grid[(y,x)] == 0:
                rb += 1
                continue
            if (y < ky) or (y == ky and x < kx): ky,kx = y,x

        # print('rb',rb,(ky,kx),c_visited)

        change = False
        if len(c_visited) > max(2,level_max): change = True
        if rb > lrb: change = True
        if rb == lrb and ky > level_key[0]: change = True 
        if rb == lrb and ky == level_key[0] and kx > level_key[1]:
            change = True
        if not change: continue

        level_max,level_group = len(c_visited),c_visited
        level_key,lrb = (ky,kx),rb            

    # print(level_max,level_group)

    return level_max,level_group

def gravity(grid):
    new_grid = dict()
    for j in range(n):
        x = n-1
        for i in range(n)[::-1]:
            v = grid.get((i,j),-2) 
            if v == -2: continue
            if v == -1: x = i
            new_grid[(x,j)] = v
            x -= 1
    return new_grid

from collections import deque
n,m = map(int,input().split())
grid = {(i,j):k for i in range(n) for j,k in enumerate(list(map(int,input().split())))}
dir = [(0,1),(1,0),(0,-1),(-1,0)]
ans = 0

while True:
    level_max,level_group = do_play(grid)
    if level_max < 2: break
    # print(level_max)
    ans += level_max**2
    for node in level_group: del grid[node]
    grid = gravity(grid)
    new_grid = {(n-j-1,i):v for (i,j),v in grid.items()}
    grid = gravity(new_grid)

print(ans)