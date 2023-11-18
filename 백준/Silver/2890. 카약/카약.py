R,C = map(int,input().split())
ex = [0]*10
for i in range(R):
    ex1 = str(input())
    ex1 = ex1[::-1]
    for j in range(len(ex1)):
        if ex1[j] not in ['S','.','F']:
            ex[int(ex1[j])] = j
            break

ex3 = list(set(ex))
ex3.sort()
for i in range(1,10):
    print(ex3.index(ex[i]))