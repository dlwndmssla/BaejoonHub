import sys
input = sys.stdin.readline
n = int(input())

thing = sorted([int(input()) for i in range(n)], reverse= True)
thing2 = [(i+1)*thing[i] for i in range(n)]
print(max(thing2))