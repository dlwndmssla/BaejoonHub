a,b = map(int, input().split())

a = b-a

k = min(a,b)

for i in range(k,0,-1):
    if a%i == 0 and b%i == 0:
        a = int(a/i)
        b = int(b/i)
        
print(a,b)