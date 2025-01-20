n = int(input())

for i in range(1,1+n):
  if i%2:
    print('* '*(n-1)+"*")
  else:
    print(' *'*n)