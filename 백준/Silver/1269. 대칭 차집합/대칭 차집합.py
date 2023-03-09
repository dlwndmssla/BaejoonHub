import sys
input = sys.stdin.readline
a ,b= map(int, input().split())
ex1= list(map(int, input().split()))
ex2= list(map(int, input().split()))
ex3 = ex1 + ex2 
ex3 = set(ex3)
print(-len(ex1)-len(ex2)+2*len(ex3))