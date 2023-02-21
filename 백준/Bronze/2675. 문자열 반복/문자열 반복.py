T = int(input())
for i in range(T):
    a,b = map(str,input().split())
    a = int(a)
    b = list(b)
    c = str()
    for j in range(len(b)):
        c += str(b[j]*a)
    print(c)