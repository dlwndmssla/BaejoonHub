n = int(input())
ex = list(map(int, input().split()))
k = 1
a = ex[0]
for i in range(1,n):
    if ex[i-1] <= ex[i]:
        k += 1
print(k)