n = int(input())
paper = list()

for i in range(n):
    a,b = map(int,input().split())
    for x in range(a,a+10):
        for y in range(b,b+10):
            paper.append((x,y))
ans = 0
paper = set(paper)
for x,y in paper:
    ans += 4-sum([((x+1,y) in paper),((x-1,y) in paper),((x,y+1) in paper), ((x,y-1) in paper)])
        
print(ans)