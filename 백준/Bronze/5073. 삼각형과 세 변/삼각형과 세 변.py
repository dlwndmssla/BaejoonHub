while True:
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    ex = set([a,b,c])
    if a+b+c-max(a,b,c) <= max(a,b,c):
        print('Invalid')
    elif len(ex) == 3:
        print('Scalene')
    elif len(ex) == 2:
        print('Isosceles')
    elif len(ex) == 1:
        print('Equilateral')
    
    