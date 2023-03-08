x = int(input())
a = 0
b = 0
for i in range(7):
    a = int(x / pow(2,6-i) )
    b += a   
    x = x % pow(2,6-i) 
    
print(b)