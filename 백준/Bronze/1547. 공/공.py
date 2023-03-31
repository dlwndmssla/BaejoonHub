import sys 
input = sys.stdin.readline
n = int(input())
ex1 = [0,1,0,0]


for i in range(n):
    a,b = map(int, input().split())
    
    x = ex1[a]
    y = ex1[b]
    ex1[b] = x
    ex1[a] = y
    
print(ex1.index(1))