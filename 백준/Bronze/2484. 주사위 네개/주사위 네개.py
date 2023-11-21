n = int(input())
ans = []
for i in range(n):
    count0 = [0]*7
    ex = list(map(int,input().split()))
    for j in range(4):
        count0[ex[j]]+=1
    if 4 in count0:
        a = 50000+ ex[0]*5000
    elif 3 in count0:
        x,y = set(ex)
        if sum(count0) == 3*x+y:
            a = 10000+x*1000
        else:
            a = 10000+y*1000
    elif {0,2} == set(count0):
        x,y = set(ex)
        a = 2000 + (x+y)*500
    elif {0,1,2} ==set(count0):
        x,y,z =set(ex)
        if x+sum(set(ex)) == sum(ex):
            a = 1000+x*100
        elif y+sum(set(ex)) == sum(ex):
            a = 1000+y*100
        else:
            a = 1000+z*100
    else:
        a = max(set(ex))*100
    ans.append(a)
    
print(max(ans))