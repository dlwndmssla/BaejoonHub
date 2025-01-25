N = int(input())
max_point = []
for i in range(N):
    dice = list(map(int,input().split()))
    sort_dice = sorted(set(dice))[::-1]
    a = [10000+sort_dice[0]*1000,1000+sum([i*(dice.count(i)==2) for i in sort_dice])*100
    ,max(sort_dice)*100][len(sort_dice)-1]
    max_point.append(a)
    
print(max(max_point))
