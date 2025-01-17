n = int(input())

a = str('')
for i in range(1,n+1):
    a = '*'*i+(n-i)*' '
    print(a[::-1])