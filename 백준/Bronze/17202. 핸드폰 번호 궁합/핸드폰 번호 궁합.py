ex1 = str(input())
ex2 = str(input())

ex = [0 for i in range(len(ex1) * 2)]
for i in range(len(ex1)):
    ex[i * 2] = int(ex1[i])
    ex[i * 2 + 1] = int(ex2[i])

for i in range(len(ex) - 2):
    ex3 = [0 for k in range(len(ex))]
    for j in range(len(ex) - 1):
        ex3[j] = (ex[j] + ex[j + 1]) % 10
    ex = ex3[0:-1]

print(str(ex[0])+str(ex[1]))