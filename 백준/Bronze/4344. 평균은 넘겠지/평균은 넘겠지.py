C = int(input())

for i in range(C):
    a = input().split()
    sum = 0.0
    for j in range(1,len(a)):
        sum += int(a[j])
    real = sum/int(a[0])
    k = 0
    
    for j in range(1,len(a)):
        if int(a[j]) > real:
            k+=1
        if j == len(a)-1:
            x = ("{:.3f}".format(k/int(a[0])*100))+"%"
            print(x)