from collections import deque

n,m = map(int,input().split())
people = list(map(int,input().split()))[1:]
party = dict()
nparty = set()
peo_to_par = {i:[] for i in range(1,n+1)}

for _ in range(m):
    p = list(map(int,input().split()))[1:]
    party[_] = p
    for i in p: peo_to_par[i].append(_)

v = deque(people)
while v:
    a = v.popleft()
    if a not in people:
        people.append(a)
    for pt in peo_to_par[a]: nparty.add(pt)

    for p in sum([party[b] for b in peo_to_par[a]],[]):         
        if p in people: continue
        people.append(p)
        v.append(p)
print(m-len(nparty))