list0 = list(map(str, 'abcdefghijklmnopqrstuvwxyz'))
list1 = [[] for i in range(len(list0))]

n = int(input())
ans = n
for i in range(n):
    ex = str(input())
    list1 = [[] for i in range(len(list0))]
    for j in range(len(ex)):
        list1[list0.index(ex[j])].append(j)
       
    for ex2 in list1:
        if ex2 != []:
            if ex2[0] +len(ex2) -1 != ex2[-1]:
                ans = ans -1
                break
print(ans)