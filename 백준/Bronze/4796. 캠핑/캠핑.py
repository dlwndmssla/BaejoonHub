def vac(a,b,c):
    week = int(c/b)*a
    weekend = min(c%b,a)
    camp = week+weekend
    
    return camp

k = 1
while True:
    a,b,c = map(int, input().split())
    
    if a==b==c==0:
        break
    else:    
        camp = vac(a,b,c)
        x = 'Case '+str(k)+':'
        k += 1
        print(x,camp)