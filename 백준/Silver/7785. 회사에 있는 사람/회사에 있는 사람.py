import sys
input = sys.stdin.readline
n = int(input())
enter = set()
for i in range(n):
    a,b = map(str, input().split())
    if b == 'enter':
        enter.add(a)
    else:
        if a in enter:
            enter.remove(a)
        
enter = list(enter)
if len(enter) != 0:
    enter.sort()
    enter.reverse()
    for i in range(len(enter)):
        print(enter[i])