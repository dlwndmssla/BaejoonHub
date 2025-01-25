ch_num = [list(map(int,input().split())) for i in range(5)]
x_num = [list(map(int,input().split())) for i in range(5)]
x_num = sum(x_num,[])
bingo = ch_num+[[ch_num[i][j] for i in range(5)] for j in range(5)] +[[ch_num[i][i] for i in range(5)],[ch_num[4-i][i] for i in range(5)]]
for i,x in enumerate(x_num):
    for cn_list in bingo:
        if x not in cn_list: continue
        cn_list.remove(x)
    if bingo.count([])>=3:
        print(i+1)
        break