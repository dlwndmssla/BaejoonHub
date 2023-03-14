import sys
input = sys.stdin.readline
a = int(input())

ex1 = list(map(int, input().split()))
ex1.sort()

n = int(input())

m  = 0
k = 0
for i in range(a-1):
    if ex1[0] > n:
        x = n-1
        y = ex1[0] - n -1
        k = x+y+x*y

    elif ex1[i] < n < ex1[i+1]:
        m = ex1[i+1] - ex1[i] 
        k = m -2 + (n-ex1[i]-1)*(ex1[i+1]-n-1)
        
        
print(k)