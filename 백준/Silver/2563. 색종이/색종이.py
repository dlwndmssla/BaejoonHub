import sys
input = sys.stdin.readline
space = []
for i in range(int(input())):
    x,y = list(map(int,input().split()))
    space.extend(sum([[ (i,j) for i in range(x,x+10)] for j in range(y,y+10)],[]))
print(len(set(space)))