stud = []
for i in range(1,31):
    stud.append(i)
    
for i in range(28):
    a = int(input())
    stud.remove(a)
    
if stud[0] > stud[1]:
    print(stud[1])
    print(stud[0])
else:
    print(stud[0])
    print(stud[1])