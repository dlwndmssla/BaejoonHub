n = int(input())

for i in range(n-1,0,-1):

    print(" "*int(n-i-1) +"*"*(i*2+1))
    
for i in range(n):
    print(" "*int(n-i-1) +"*"*(i*2+1))