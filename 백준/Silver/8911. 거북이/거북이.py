import sys
input = sys.stdin.readline

def turning(dir0,c): #change - 바뀌는 방향
    if c == 'R':
        dir = dir1[(dir1.index(dir0)+1)%4]
    else:
        dir = dir1[dir1.index(dir0)-1]
    return dir

def going(tur_y,tur_x,t,dir): #change - 바뀌는 방향
    if t == 'F':
        tur_y,tur_x = tur_y+dir[0],tur_x+dir[1]
    else:
        tur_y,tur_x = tur_y-dir[0],tur_x-dir[1]
    return tur_y,tur_x 

def one_game(route):
    tur_y,tur_x = 0,0
    turtle_points = [[tur_y,tur_x]]
    dir = [-1,0]

    for t in route:
        if t in ['F','B']:
            tur_y,tur_x = going(tur_y,tur_x,t,dir)
            turtle_points.append([tur_y,tur_x])
        else:
            dir = turning(dir,t)

    points_T = [list(i) for i in zip(*turtle_points)]
    print((max(points_T[0])-min(points_T[0]))*(max(points_T[1])-min(points_T[1])))


dir1 = [[-1,0],[0,1],[1,0],[0,-1]] #dy,dx
for _ in range(int(input())):
    route = str(input())
    one_game(route)
