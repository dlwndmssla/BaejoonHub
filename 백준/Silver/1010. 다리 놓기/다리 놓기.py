t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    cross = 1
    if n != m:
        for j in range(1,m+1):
            cross = cross*j
        for k in range(1,n+1):
            cross = cross/k
        for h in range(1,m-n+1):
            cross = cross/h
        print(round(cross))
    else:
        print(1)