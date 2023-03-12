import sys
input = sys.stdin.readline
N = int(input())

for i in range(N):
    a = int(input())
    b = int(input())
    ex1 = [i for i in range(1,b+1)]
    ex2 = []
    for j in range(a):
        for k in range(b):
            ex2.append(sum(ex1[:k+1])) 
        ex1 = ex2
        ex2 = []   
    print(ex1[-1]) 