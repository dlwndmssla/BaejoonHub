import sys
input = sys.stdin.readline
a,b = map(int, input().split())
ex1 = list(map(int, input().split()))
ex1.sort()
print(ex1[b-1])