king, stone, n = map(str,input().split())
moving = [str(input()) for i in range(int(n))]

dirs = {'R':(0,1), 'L':(0,-1), 'B':(-1,0), 'T':(1,0),'RB':(-1,1), 'LB':(-1,-1), 'RT':(1,1), 'LT':(1,-1)}
alpha = 'ABCDEFGH'

kx,ky = alpha.index(king[0]), int(king[1])-1
sx,sy = alpha.index(stone[0]), int(stone[1])-1


for a in moving: 
    dy,dx = dirs[a]
    # print()
    # print(alpha[kx]+str(ky+1))
    # print(alpha[sx]+str(sy+1))  
    ky1,kx1,sy1,sx1 = ky+dy,kx+dx,sy+dy,sx+dx
    
    # print(a, f"dx,dy = {[dx,dy]}")
    if bool(set([ky1,kx1]) & set([-1,8])): continue
    sb1 = ((ky1,kx1) == (sy,sx)) 
    sb2 = not bool(set([sy1,sx1]) & set([-1,8]))   

    if sb1 and not sb2: continue
    ky,kx = ky1,kx1
    sy,sx = sy+dy*sb1*sb2,sx+dx*sb1*sb2
    
# print()
print(alpha[kx]+str(ky+1))
print(alpha[sx]+str(sy+1))  


