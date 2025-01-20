import math 
n = int(input())

if n == 1:
  print('*')
else:

  for _ in range(n):
    print("* "*(math.ceil(n/2)-1)+'*')
    print(" *"*(math.floor(n/2)))