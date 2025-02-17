from itertools import product

def find_extent(points):
    points_T = list(list(i) for i in zip(*points))
    max_y,min_y = max(points_T[0]),min(points_T[0])
    max_x,min_x = max(points_T[1]),min(points_T[1])
    width_y,width_x = max_y-min_y,max_x-min_x
    big_square = width_y*width_x
    
    return list(product([max_y,min_y],[max_x,min_x])), big_square


dir0 = [0,[0,-1],[0,1],[ 1,0],[-1,0]] #동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로
cur_y,cur_x = 0,0
points = [[cur_y,cur_x ]]

n = int(input())
for _ in range(6):
    t, dist = list(map(int,input().split()))
    dy,dx = dir0[t]
    cur_y,cur_x = cur_y+dy*dist,cur_x+dx*dist
    points.append([cur_y,cur_x ])

big_node, big_space = find_extent(points)

for y2,x2 in big_node:
    if list([y2,x2]) not in points: break
small_node = [[y2,x2]]
for node in points:
    if tuple(node) not in big_node:
        small_node.append(node)

small_node, small_space = find_extent(small_node)
print((big_space-small_space)*n)
