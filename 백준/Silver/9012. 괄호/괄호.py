for i in range(int(input())):
    a = str(input())
    b = len(a)
    c = 0
    ex1 = []
    for j in range(b):
        if a[j] == '(':
            c += 1
        else:
            c -= 1
        ex1.append(c)
 
    if -1 in ex1:
        print('NO')
    elif ex1[-1] != 0:
        print('NO')
    else:
        print('YES')
        