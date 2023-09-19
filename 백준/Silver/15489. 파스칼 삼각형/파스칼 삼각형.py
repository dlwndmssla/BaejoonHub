r,c,w = map(int,input().split())
ex = [[] for i in range(r+w)]
for i in range(len(ex)):
    for j in range(i+1):
        if j == 0:
            ex[i].append(1)
        elif j == i:
            ex[i].append(1)
        else:
            ex[i].append(ex[i-1][j-1]+ex[i-1][j])
            
ans = sum([ sum(ex[r-1+x][c-1:c+x]) for x in range(w)])
print(ans)