n,m = map(int,input().split())
r,c,d = map(int,input().split())
room = {(i,j):k for i in range(n) for j,k in enumerate(list(map(int,input().split())))}

dir = [(-1,0),(0,1),(1,0),(0,-1)]

cnt = 0
while True:
    if room[(r,c)] == 0:
        room[(r,c)] = 2
        cnt += 1
    cross = [room.get((r+dr,c+dc),3) for dr,dc in dir]
    if 0 not in cross:
        dy,dx = dir[d]
        r,c = r-dy,c-dx
        if room.get((r,c),3) in [1,3]: break
    else:
        for k in range(1,4+1):
            d0 = (d-k)%4
            dy0,dx0 = dir[d0]
            r0,c0 = r+dy0,c+dx0
            if room.get((r0,c0),3) == 0:
                r,c,d = r0,c0,d0
                break
print(cnt)