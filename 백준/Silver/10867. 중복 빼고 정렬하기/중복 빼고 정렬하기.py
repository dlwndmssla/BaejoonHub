import sys
#input = sys.stdin.readline
a = int(input())
ex1 = list(map(int, input().split()))
ex1 = list(set(ex1))
ex1.sort()
print(*ex1)