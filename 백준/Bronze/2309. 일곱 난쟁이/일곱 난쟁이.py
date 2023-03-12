import sys
input = sys.stdin.readline
a = []
for k in range(9):
    a.append(int(input()))
a.sort()

b = sum(a)
for i in range(8):
    for j in range(i+1,9):
        c = b - a[i] - a[j]    
        if c == 100:
            break
    if c == 100:
            break

ex1 = a
ex1.remove(a[j])
ex1.remove(a[i])

for k in range(len(ex1)):
    print(ex1[k])