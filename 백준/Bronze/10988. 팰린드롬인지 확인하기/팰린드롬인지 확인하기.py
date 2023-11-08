ex = str(input())
n = len(ex)
a = 0
for i in range(n):
    if ex[i] != ex[n-i-1]:
        a += 1
    if a > 0:
        break
    
if a > 0:
    print(0)
else:
    print(1)