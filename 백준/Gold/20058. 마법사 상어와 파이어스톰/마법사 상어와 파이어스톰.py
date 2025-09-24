from collections import deque

global dir
dir = [(0,1),(-1,0),(0,-1),(1,0)]

def new(y,x,v,ice):
    if not v: return v
    ice_red = 0
    for dy,dx in dir:
        y1,x1 = y+dy,x+dx
        ice_red += not ice.get((y1,x1),0)
        if ice_red >= 2:
            return max(v-1,0)
    
    return v

def do_magic(l,ice):

    w = 2**l
    ice = {(w*(i//w)+j%w,w*(j//w)+w-i%w-1):v for (i,j),v in ice.items()}
    new_ice = {(y,x): new(y,x,v,ice) for (y,x),v in ice.items()}

    return new_ice
        

def find_ice(k,ice):
    a = 0
    queue = deque([k])
    while queue:
        (y,x) = queue.pop()
        for dy,dx in dir:
            k = (y+dy,x+dx)
            v = ice.get(k,0)
            if not v: continue
            a += 1
            ice[k] = 0
            queue.append(k)

    return ice,a


def find_ans(magic,ice):
    for l in magic: ice = do_magic(l,ice)
    print(sum(ice.values()))
    
    ans = 0
    for k,v in ice.items():
        if not v: continue
        ice,a = find_ice(k,ice)
        ans = max(ans,a)
    print(ans)


n,q = list(map(int,input().split()))
width = 2**n

ice = {(i,j):v for i in range(width) for j,v in enumerate(list(map(int,input().split())))}
magic = list(map(int,input().split()))

find_ans(magic,ice)

