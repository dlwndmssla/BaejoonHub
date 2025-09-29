
def move_cloud(m,cloud):
    d,s = m
    (dy,dx) = dirs[d-1]
    dy *= s
    dx *= s
    return set(((y+dy)%n,(x+dx)%n) for y,x in cloud)


def rain(cloud,water):
    for k in cloud: water[k] += 1

    for (y,x) in cloud:
        for (dy,dx) in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            if not 0<=y+dy<=n-1 or not 0<=x+dx<=n-1: continue
            if not water[(y+dy,x+dx)]: continue
            water[(y,x)] += 1

    new_cloud = set()
    for k,v in water.items():
        if not v >= 2 or k in cloud: continue
        water[k] -= 2
        new_cloud.add(k)

    return new_cloud,water


global dirs,n
dirs = {0: (0, -1), 1: (-1, -1), 2: (-1, 0), 3: (-1, 1), 4: (0, 1), 5: (1, 1), 6: (1, 0), 7: (1, -1)}

n,m = list(map(int,input().split()))
water = {(i,j):v for i in range(n) for j,v in enumerate(list(map(int,input().split())))}

cloud = {(n-1,0),(n-1,1),(n-2,0),(n-2,1)}

for i in range(m):
    magic = list(map(int,input().split()))
    cloud = move_cloud(magic,cloud)
    cloud,water = rain(cloud,water)
print(sum(water.values()))