import sys
input = sys.stdin.readline
a,b = map(int, input().split())
ex1 = set()
ex2 = set()

for i in range(a):
    ex1.add(input().rstrip())
for i in range(b):
    ex2.add(input().rstrip())

x = []

if a >= b:
    for i in ex2:
        if i in ex1:
            x.append(i)      
else:
    for i in ex1:
        if i in ex2:
            x.append(i)
            
x.sort()
print(len(x))
for i in x:
    print(i)