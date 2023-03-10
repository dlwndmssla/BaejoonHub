a,b = map(int, input().split())

ex1 = [0,31,28,31,30,31,30,31,31,30,31,30,31]
ex2 = [ 'SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
c = sum(ex1[:a])+b
print(ex2[c%7])