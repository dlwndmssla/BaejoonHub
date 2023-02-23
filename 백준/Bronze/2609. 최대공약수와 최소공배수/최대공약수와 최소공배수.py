a,b = map(int, input().split())
lista = [a]
for i in range(2, int(a/2)+2):
    if a%i == 0:
        lista.append(i)
listb = [b]
for i in range(2, int(b/2)+2):
    if b%i == 0:
        listb.append(i)
listc = []
for i in range(len(lista)):
    for j in range(len(listb)):
        if lista[i] == listb[j]:
            listc.append(lista[i])
if len(listc) != 0:  
    c = max(listc)
    print(c)
    print(int(a*b/c))
else:
    print(1)
    print(a*b)