from collections import deque

global dir,n
dir = [(0,1),(-1,0),(0,-1),(1,0)]

def new(k,v,ice):
    if not v: return v
    (y,x),ice_red = k,0
    for dy,dx in dir:
        ice_red += not ice.get((y+dy,x+dx),0)
        if ice_red >= 2: return max(v-1,0)
    return v

def do_magic(l,ice):

    w,t = 2**l,2**n
    ice = {(w*(i//w)+j%w,w*(j//w)+w-i%w-1):v for (i,j),v in ice.items()}
    melt = dict()
    for k,v in ice.items():
        a = melt.get(k,0)+k.count(0)+k.count(t-1)
        if a: melt[k] = a
        if v: continue
        for dy,dx in dir:
            k1 = (k[0]+dy,k[1]+dx) 
            if k1 not in ice: continue
            melt[k1] = melt.get(k1,0)+1
    for k,v in melt.items(): ice[k] = max(ice[k]-(v>=2),0)
    return ice
        

def find_ice(k,ice):
    queue,a = deque([k]),0
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
ice = {(i,j):v for i in range(2**n) for j,v in enumerate(list(map(int,input().split())))}
magic = list(map(int,input().split()))

find_ans(magic,ice)

