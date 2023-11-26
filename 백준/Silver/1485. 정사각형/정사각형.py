n = int(input())
for i in range(n):
    con = 1
    ex = []
    for j in range(4):
        ex.append(list(map(int,input().split())))
    a,b = ex[0]
    ex0 = []
    for k in range(1,4):
        aa,bb = ex[k]
        ex0.append(pow(a-aa,2)+pow(b-bb,2))
    
    ex0.sort()
    con = (len(set(ex0)) == 2)
    if con:
        for q in [1,2,3]:
            a,b = ex[q]
            ex1 = []
            for k in range(4):
                if q ==k: continue
                aa,bb = ex[k]
                ex1.append(pow(a-aa,2)+pow(b-bb,2))
            ex1.sort()
            if ex1 == ex0: continue
            else:
                con = 0
                break
    if con == 1:
        print(1)
    else:
        print(0)