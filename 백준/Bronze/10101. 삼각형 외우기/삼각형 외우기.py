a = int(input())
b = int(input())
c = int(input())

ex = set([a,b,c])
if a+b+c != 180:
    print('Error')
elif a==b==c==60:
    print('Equilateral')
elif len(ex) == 2:
    print('Isosceles')
elif len(ex) == 3:
        print('Scalene')