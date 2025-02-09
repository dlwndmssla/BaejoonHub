import copy

def turning(dir0,c): #change - 바뀌는 방향
    direction = [[-1,0],[0,1],[1,0],[0,-1]] #dy,dx
    if c == 'R':
        dir = direction[(direction.index(dir0)+1)%4]
    else:
        dir = direction[direction.index(dir0)-1]
    return dir

for _ in range(int(input())):
    route = str(input())
    turtle = [0,0]
    turtle_points = [[0,0]]
    dir = [-1,0]
    for t in route:
        if t == 'F':
            turtle[0] += dir[0]
            turtle[1] += dir[1]
            turtle_points.append(copy.copy(turtle))
        elif t == 'B':
            turtle[0] += -dir[0]
            turtle[1] += -dir[1]
            turtle_points.append(copy.copy(turtle))    
        else:
            dir = turning(dir,t)
        # print(turtle,dir)
            
    # print(turtle_points)
    points_T = [list(i) for i in zip(*turtle_points)]
    print((max(points_T[0])-min(points_T[0]))*(max(points_T[1])-min(points_T[1])))
