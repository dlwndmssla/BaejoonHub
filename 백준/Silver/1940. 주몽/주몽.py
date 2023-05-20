a = int(input())
b = int(input())
ex = list(map(int, input().split()))
k = 0
ex.sort()

for i in range(a-1):
    for j in range(a-1, i,-1):
        if ex[i]+ ex[j] == b and ex[i] != b and ex[j]!= b:
            ex[i] = 0
            ex[j] = 0
            k += 1
            break
print(k)