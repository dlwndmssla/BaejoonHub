a = int(input())
b = str(input())
d = 0
for i in range(3):
    c = a*int(b[2-i])
    print(c)
    d += c*pow(10,i)
    
print(d)