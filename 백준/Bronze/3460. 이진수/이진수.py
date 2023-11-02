n = int(input())
ans = []
for i in range(n):
    b = int(input())
    a = list(map(str,bin(b)))
    a = a[::-1]
    for j in range(len(a)):
        if a[j] == '1':
            ans.append(j)
    
print(*ans)