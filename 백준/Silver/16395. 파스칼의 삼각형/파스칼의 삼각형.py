n,k = map(int,input().split())
pascal = []
for i in range(n):
    ex = []
    for j in range(i+1):
        if j == 0 or j == i:
            ex.append(1)
        else:
            ex.append(pascal[-1][j-1]+pascal[-1][j])

    pascal.append(ex)

print(pascal[-1][k-1])