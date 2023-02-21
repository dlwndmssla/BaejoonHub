A,B,V = map(int, input().split())

c = int((V-A)/(A-B)) 

if c ==  (V-A)/(A-B):
    print(c +1)
    
else:
    print(c +2 )