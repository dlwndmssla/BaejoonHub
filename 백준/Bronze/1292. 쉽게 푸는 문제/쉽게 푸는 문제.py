A,B = map(int, input().split())

list = []
k = 0
for i in range(1, B):
    k = i
    for j in range(i):
        list.append(k)
    
if B != 1:        
    sum = 0
    for i in range(A-1,B):
        sum += list[i]

    print(sum)
else:
    print(1)