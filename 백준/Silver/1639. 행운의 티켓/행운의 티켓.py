a = str(input())
n = len(a)
ticket = [0]
for i in range(n):
    k = ticket[i] + int(a[i])
    ticket.append(k)

x = 0
for i in range(n):
    for j in range(1,n):
        if i+j*2 < n+1:
            if ticket[i+j]-ticket[i] == ticket[i+j*2]-ticket[i+j] and x < j:
                x = j
        else:
            break     
print(x*2)   