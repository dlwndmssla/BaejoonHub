n = int(input())

for i in range(n):
    m = int(input())
    ex0,ex1 = [],[]
    for j in range(m):
        b,a = map(str,input().split())
        if a not in ex0:
            ex0.append(a)
            ex1.append([b])
        else:
            idx = ex0.index(a)
            ex1[idx].append(b)
            
    ans = 1
    for k in range(len(ex1)):
        ans = ans*(len(ex1[k])+1)
    print(ans -1)