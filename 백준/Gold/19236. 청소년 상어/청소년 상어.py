def turn(f,grid,fish):
    y,x = fish.get(f)
    f,d = grid.get((y,x))
    for k in range(8):
        dy,dx = dirs[(d+k)%8]
        f2,d2 = grid.get((y+dy,x+dx),(-1,-1))
        if -1 in (f2,d2): continue 
        return (d+k)%8
    return (d+1)%8

def fish_moving(grid,fish,eat):
    for f in range(1,1+16):
        if f in eat.values(): continue
        d = turn(f,grid,fish)
        y,x = fish.get(f)
        dy,dx = dirs[d]
        y1,x1 = y+dy,x+dx
        f1,d1 = grid.get((y1,x1),(-1,-1))
        if -1 in (f1,d1): continue
        grid[(y1,x1)],grid[(y,x)] = (f,d),(f1,d1)
        fish[f],fish[f1] = (y1,x1),(y,x)
        y,x = y1,x1

    return grid,fish

def eating(shark,shark1,grid,fish,eat):
    f,d = grid.get(shark1,(-1,-1))
    grid1 = {k:v for k,v in grid.items()}
    fish1 = {k:v for k,v in fish.items()}
    eat1 = {k:v for k,v in eat.items()}
    eat1[len(eat)] = f
    grid1[shark1] = (-1,d)
    del fish1[f]
    grid1[shark] = ('*',0)
    grid1,fish1 = fish_moving(grid1,fish1,eat1)
    return grid1,fish1,eat1


def tracking(shark,grid,fish,eat):
    global ans
    (s,sd),(y,x)  = grid[shark],shark
    dy,dx = dirs[sd]
    if sum(eat.values()) > sum(ans.values()):
        ans = {k:v for k,v in eat.items()}

    for k in [1,2,3]:
        y1,x1 = y+dy*k,x+dx*k
        if not (0 <= y1 <= 3): continue
        if not (0 <= x1 <= 3): continue
        f,d = grid.get((y1,x1),(-1,-1))
        if f == '*': continue
        if f in eat.values(): continue 
        grid1,fish1,eat1 = eating(shark,(y1,x1),grid,fish,eat)
        tracking((y1,x1),grid1,fish1,eat1)



global dirs
dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

grid,fish = dict(),dict()
for i in range(4):
    x = list(map(int,input().split()))
    for j,(a,b) in enumerate(zip(x[::2],x[1::2])):
        grid[(i,j)] = (a,b-1)
        fish[a] = (i,j)

s,shark = -1,(0,0)
e,sd = grid[shark]
grid[shark] = (s,sd)
eat,ans = {0:e},{0:e}

grid,fish = fish_moving(grid,fish,eat)
tracking(shark,grid,fish,eat)
print(sum(ans.values()))
