import sys
input = sys.stdin.readline
a = []
for i in range(9):
    a += list(map(int, input().split()))
    
k = a.index(max(a))    
print(max(a))
print(int(k/9)+1,k%9+1)
