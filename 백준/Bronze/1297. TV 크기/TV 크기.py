import sys,math
input = sys.stdin.readline
D,H,W = map(int, input().split())
k = math.sqrt(H*H+W*W)
a = int(D*H/k)
b = int(D*W/k)
print(a,b)