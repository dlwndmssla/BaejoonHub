a = str(input())
# print(a)

quack_idx = [0,0,0,0,0]
quack_idx2 = [0,0,0,0,0]
duck_max = -1
for i in a:
    idx = 'quack'.index(i)
    quack_idx2[idx] += 1
    if idx == 0 or quack_idx[idx-1] > quack_idx[idx]:
        quack_idx[idx] += 1
        duck_max = max(duck_max,quack_idx[0]-quack_idx[-1])

if quack_idx[0] == quack_idx[-1] and len(set(quack_idx2)) == 1:
    print(duck_max)
else:
    print(-1)
    