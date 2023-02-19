x = int(input())

i = 1
sum = 0
k = []
while True:
    
    sum += i
    k.append(sum) 
    
    i += 1
    
    if sum >= x:
        a = str(sum - x+1)+"/"+str(i-sum +x-1)
        if i%2 == 0:
            a = str(sum - x+1)+"/"+str(i-sum +x-1)
        else:
            a = str(i-sum +x-1) +"/"+ str(sum - x+1)
        print(a)
        break    