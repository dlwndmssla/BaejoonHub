import sys
input = sys.stdin.readline
a,b = map(int, input().split())
ex1 = []
for i in range(2*a):
    ex1.append(list(map(int,input().split())))
for i in range(a):
    ex2 = []   
    for j in range(b):
        ex2.append(ex1[i][j] +ex1[i+a][j])
    print(*ex2)