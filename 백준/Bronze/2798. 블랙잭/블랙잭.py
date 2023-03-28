import sys
input=sys.stdin.readline
a,b = map(int, input().split())
ex1 = list(map(int, input().split()))
i_list = []
j_list = []
k_list = []
for i in range(a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            i_list.append(i)
            j_list.append(j)
            k_list.append(k)
x = 0
for z in range(len(i_list)):
    y = ex1[i_list[z]]+ex1[j_list[z]]+ex1[k_list[z]]
    if x < y  <=b:
        x = y
        
    if x == b:
        break
    
print(x)