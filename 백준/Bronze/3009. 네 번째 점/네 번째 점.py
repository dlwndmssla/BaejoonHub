ex1 = []
ex2 = []

for i in range(3):
    a,b = map(int, input().split())
    ex1.append(a)
    ex2.append(b)

ex3 = []

if ex1[0] == ex1[1]:
    ex3.append(ex1[2])
elif ex1[0] == ex1[2]:
    ex3.append(ex1[1])
else:
    ex3.append(ex1[0])
    
if ex2[0] == ex2[1]:
    ex3.append(ex2[2])
elif ex2[0] == ex2[2]:
    ex3.append(ex2[1])
else:
    ex3.append(ex2[0])
    
print(*ex3)