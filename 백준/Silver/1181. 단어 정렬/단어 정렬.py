n = int(input())
ex = list()

for i in range(n):
    a = str(input())
    ex.append([a, len(a)])

ex.sort(key=lambda x : ( x[1], x[0]) )

print(ex[0][0])
for i in range(1,len(ex)):
    if ex[i] !=ex[i-1]:
        print(ex[i][0])