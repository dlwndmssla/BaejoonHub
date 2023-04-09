import sys
input = sys.stdin.readline
ex1 = input().rstrip().lower()
ex2 = set(ex1)
count = []
for i in ex2:
    count.append(ex1.count(i))

if count.count(max(count)) == 1:
    x = list(ex2)[count.index(max(count))].upper()
    print(x)
else:
    print('?')