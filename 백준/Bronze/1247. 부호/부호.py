for i in range(3):
    a = int(input())
    k = 0
    for i in range(a):
        b = int(input())
        k += b
        
    if k == 0:
        print(0)
    elif k > 0:
        print("+")
    else:
        print('-')