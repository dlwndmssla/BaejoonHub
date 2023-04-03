import sys
input = sys.stdin.readline
a,b = map(int, input().split())
pascal = [0]
for i in range(a):
    x = [1]*(i+1)
    pascal.append(x)
    
for i in range(3,1+a):
    for j in range(len(pascal[i])):
        if j !=0 and j != len(pascal[i])-1:
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

print(pascal[-1][b-1])