N = int(input())
a = 0
b = 1

if N == 0:
    c = 0
elif N == 1:
    c = 1
else:
    for i in range(1,N):
        c = a+b
        a = b
        b = c

print(c)