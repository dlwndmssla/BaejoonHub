import sys
input = sys.stdin.readline
ex = []
for i in range(7):
    a = int(input())
    if a%2 == 1:
        ex.append(a)
        
if len(ex) > 0:
    print(sum(ex))
    print(min(ex))
else:
    print(-1)