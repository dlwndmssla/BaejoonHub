
def moveing(n):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    cnt = n*n
    y,x = (1,1)
    grid = {(y,x):cnt}
    cnt -= 1
    d = 0
    dy,dx = dir[d]
    while True:
        y1,x1 = dy+y,dx+x
        if not 1<= y1 <=n or not 1<= x1 <=n or grid.get((y1,x1),0):
            d = (d+1)%4
            dy,dx = dir[d]
            continue
        grid[(y1,x1)] = cnt
        cnt -= 1
        y,x = y1,x1
        if not cnt: break

    return {k:v for v,k in grid.items()}

n = int(input())
sand = {(i+1,j+1):v for i in range(n) for j,v in enumerate(list(map(int,input().split())))}
move = {(3,0):0.05,(2,1):0.1,(2,-1):0.1,(1,1):0.07,(1,-1):0.07,(1,2):0.02,(1,-2):0.02,(0,1):0.01,(0,-1):0.01,(2,0):0}

grid = moveing(n)

ans = 0
for i in range(1,n*n):
    (y,x),(y1,x1) = grid[i+1],grid[i]
    dy,dx = y-y1,x-x1
    ty,tx = 1-abs(dy),1-abs(dx)
    s,s0 = sand[(y,x)],sand[(y,x)]


    for (d,t),v in move.items():
        y2,x2 = y1+dy*d+ty*t,x1+dx*d+tx*t
        a = int(v*s)
        if not v: a = s0
        s0 -= a
        if not (1<= y2 <=n) or not (1<= x2 <=n):
            ans +=a
            continue
        sand[(y2,x2)] += a

    sand[(y,x)] = 0

print(ans)

