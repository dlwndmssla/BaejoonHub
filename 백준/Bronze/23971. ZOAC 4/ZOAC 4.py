w,h,n,m = map(int,input().split())

if h%(m+1) == 0:
    a = h/(m+1)
else:
    a = int(h/(m+1))+1
    

if w%(n+1) == 0:
    b = w/(n+1)
else:
    b = int(w/(n+1))+1
    
print(int(a*b))