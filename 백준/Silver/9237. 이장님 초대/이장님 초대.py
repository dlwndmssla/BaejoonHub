import sys
input = sys.stdin.readline
n = int(input())
tree = list(map(int, input().split()))

tree.sort()
tree.reverse()
day = []
x = n
for i in range(n):
    if (tree[i]+i+2 > x):
        x = tree[i]+i+2
        
print(x)