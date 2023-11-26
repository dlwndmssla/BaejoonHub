n,game = map(str,input().split())
n = int(n)
ex = []
for i in range(n):
    ex.append(str(input()))
    
ex = set(ex)
a = [0,'Y','F','O'].index(game)
print(int(len(ex)/a))