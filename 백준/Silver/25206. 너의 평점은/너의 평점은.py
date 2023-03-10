ex1 = []   #분자
ex2 = []   #분모
ex3 = ['A+', 'A0','B+','B0','C+','C0', 'D+','D0', 'F']
ex4 = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]
d = set(ex3)

for i in range(20):
    obj = list(map(str,input().split()))
    if obj[2] in d:
        ex2.append(obj[1])
        ind = ex3.index(obj[2])
        ex1.append(ex4[ind])
    
ex2 = list(map(float, ex2))
up = sum(ex1[i]*ex2[i] for i in range(len(ex2)))
down = sum(ex2)
print(round(up/down,5))