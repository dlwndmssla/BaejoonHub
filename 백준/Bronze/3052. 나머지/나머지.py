list = []
a = 0
for i in range(10):
    a = int(input())%42
    list.append(a)
    
a = set(list)
print(len(a))