n,m = list(map(int,input().split()))
dna_list = sorted([input() for i in range(n)])


ans = ''
cnt = 0
for i in zip(*dna_list):
    cnt_list = list((list(i).count(j) for j in 'ACGT'))
    max_idx = cnt_list.index(max(cnt_list))
    ans += 'ACGT'[max_idx]
    cnt += n-max(cnt_list)
print(ans)  
print(cnt)  