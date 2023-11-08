a,b,c = map(int,input().split())
n = int(input())


a0 = int(n/3600)
n = n%3600
b0 = int(n/60)
c0 = n%60

a += a0
b += b0
c += c0

b += int(c/60)
c = c%60
a = (a+int(b/60))%24
b = b%60
print(a,b,c)