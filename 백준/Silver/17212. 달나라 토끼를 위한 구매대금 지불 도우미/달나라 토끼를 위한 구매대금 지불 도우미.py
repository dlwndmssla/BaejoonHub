n = int(input())
ex = [0]*max((n+1),8)
ex = [0]*max((n+1),8)
ex[1] = 1
ex[2] = 1
ex[5] = 1
ex[7] = 1

def coin(i):
    for j in [1,2,5,7]:
        if i+j >n:continue
        if ex[i+j] !=0:
            ex[i+j] = min(ex[i]+1,ex[i+j])
        else:
            ex[i+j] = ex[i]+1
    return ex

for i in range(1,n+1):
    ex = coin(i)
    
print(ex[n])