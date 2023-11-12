n = int(input())
paper = list()

for i in range(n):
    a,b = map(int,input().split())
    for x in range(a,a+10):
        for y in range(b,b+10):
            paper.append((x,y))
            
print(len(set(paper)))
