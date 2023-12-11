while True:
    n = str(input())
    if n == '0': break
    k = len(n)
    for i in range(k):
        a = sum([int(n[j]) for j in range(len(n))])
        n = str(a)
        if int(n)< 10:break
        
    print(int(n))