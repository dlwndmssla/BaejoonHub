import sys
input = sys.stdin.readline

ex = []
x = 1
y = 1
for i in range(4):
    ex.append(list(map(int, input().split())))
    
x_ran = set()
y_ran = set()
for i in range(4):
    for j in range(ex[i][0],ex[i][2]):
        x_ran.add(j)
        
    for k in range(ex[i][1],ex[i][3]):
        y_ran.add(k)
        
ans = [[0 for i in range(len(x_ran))] for i in range(len(y_ran))]
x_ran = list(x_ran)
y_ran= list(y_ran)
a_list = []
b_list = []
for i in range(4):
    for k in range(ex[i][1],ex[i][3]):
        for j in range(ex[i][0],ex[i][2]):
            b,a = y_ran.index(k),x_ran.index(j)
            a_list.append(a)
            b_list.append(b)
            
for t in range(len(a_list)):
    ans[b_list[t]][a_list[t]] = 1

final=0
for i in range(len(y_ran)):
    final += sum(ans[i])
    
print(final)
