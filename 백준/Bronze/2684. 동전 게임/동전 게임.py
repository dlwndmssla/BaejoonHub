exam = ["TTT","TTH","THT","THH","HTT","HTH","HHT","HHH"]

number = [0,0,0,0,0,0,0,0]

k = int(input())
for i in range(k):
    number = [0,0,0,0,0,0,0,0]
    a = str(input())
    
    for j in range(38):
        
        b = str(a[j]) +str(a[j+1])+str(a[j+2])
        for e in range(8):
            if exam[e] == b:
                number[e] +=1

    print(*number)