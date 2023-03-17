import sys
input = sys.stdin.readline
a,b = map(int, input().split())
k = 0
for i in range(1, a+1):
    if a%i == 0:
        k += 1
    
    if k == b:
        break
    
if k == b:
    print(i)
else:
    print(0)