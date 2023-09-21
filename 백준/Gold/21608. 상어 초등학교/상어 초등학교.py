import sys
input=sys.stdin.readline

n = int(input())
ex = []
for i in range(n*n):
    ex1 = list(map(int,input().split()))
    ex.append(ex1)

matrix = [[ 0 for i in range(n)] for j in range(n)]

for k in range(n*n):
    max0 = 0
    max_list = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0: continue
            cnt = []
            if j != 0:
                cnt.append(matrix[i][j-1])
            if j != n-1:
                cnt.append(matrix[i][j+1])
            if i !=0 :
                cnt.append(matrix[i-1][j])
            if i != n-1 :
                cnt.append(matrix[i+1][j])
            cnt0 = 0
            zero0 = 0
            for x in cnt:
                if x in ex[k][1:]:
                    cnt0 += ex[k][1:].count(x)
            if cnt0 > max0:
                max0 = cnt0
                max_list = [[i,j, cnt.count(0)]]
            elif cnt0 == max0:
                max_list.append([i,j, cnt.count(0)])
    max_list.sort(key=lambda x :x[2], reverse = True)
    x0,y0 = max_list[0][0:2]
    matrix[x0][y0] = ex[k][0]
    
ex.sort(key= lambda x : x[0])

like = 0
for i in range(n):
    for j in range(n):
        ex2 = ex[matrix[i][j]-1][1:]
        cnt = 0
        if j != 0:
            cnt += ex2.count(matrix[i][j-1])
        if j != n-1:
            cnt += ex2.count(matrix[i][j+1])
        if i !=0 :
            cnt += ex2.count(matrix[i-1][j])
        if i != n-1 :
            cnt += ex2.count(matrix[i+1][j])
        like += [0,1,10,100,1000][cnt]
print(like)