ex = str(input())

ans1 = 0
ans2 = 0
list0 = ['c=','c-','d-','lj','nj','s=','z=']
for i in range(len(ex)-2):
    if ex[i:i+3] == 'dz=':
        ans2 += 1
            
for i in range(len(ex)-1):
    if ex[i:i+2] in list0:
        ans1 += 1  
            
ans1 -= ans2
ans = len(ex)-ans1-ans2*2           
print(ans)