global n,grid,boom

def booming(ball):
    k,new_ball,g = 0,dict(),[]
    while True:
        v = ball.get(k,0)
        k += 1
        if not v and k > 1: continue
        if v in g: g.append(v); continue
        if len(g) < 4:
            new_ball.update({y:g[0] for y in range(len(new_ball),len(new_ball)+len(g))})
        else: boom[g[0]] += len(g) 
        g = [v]
        if v != -1: continue 
        new_ball[len(new_ball)] = v
        return new_ball

    
def next_ball(ball):
    k,v,new_ball,g,l = 0,0,{},[0],-1
    while l < n*n and v != -1:
        v = ball.get(k,0)
        k += 1
        if v in g: g.append(v); continue
        new_ball[l] = len(g)
        new_ball[l+1] = g[0]
        g = [v]
        l += 2

    new_ball.pop(-1)
    return new_ball


def do_boom(m,ball):
    dirs,(d,s) = {1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)},m
    dy,dx = dirs[d]
    for s0 in range(1,s+1):
        ball_k = grid[(dy*s0+int(n/2),dx*s0+int(n/2))]
        ball.pop(ball_k, None)

    ball[max(ball.keys())+1] = -1

    while True:
        new_ball = booming(ball)
        if new_ball == ball: break
        ball = new_ball
    new_ball = next_ball(ball)
    return new_ball

def moveing(n):
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    cnt,(y,x),d = n*n-1,(0,0),0
    grid = {(y,x):cnt}
    cnt -= 1
    dy,dx = dirs[d]
    while True:
        y1,x1 = dy+y,dx+x
        if not 0<= y1 <=n-1 or not 0<= x1 <=n-1 or (y1,x1) in grid:
            d = (d+1)%4
            dy,dx = dirs[d]
            continue
        grid[(y1,x1)],y,x = cnt,y1,x1
        cnt -= 1
        if cnt < 0: break

    return grid

boom = {1:0, 2:0, 3:0}
n,m = list(map(int,input().split()))
grid = moveing(n)
ball = {grid[(i,j)]:v for i in range(n) for j,v in enumerate(list(map(int,input().split()))) if v}
for _ in range(m):
    if not ball: break
    x = list(map(int,input().split()))
    ball = do_boom(x,ball)

print(sum([k*v for k,v in boom.items()]))
