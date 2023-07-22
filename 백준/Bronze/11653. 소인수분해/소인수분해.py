import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N = int(input())
m = 2
while N!=1:  
    if N%m==0: 
        print(m) 
        N = N//m
    else:
        m += 1