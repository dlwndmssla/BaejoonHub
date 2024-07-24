import sys
# input = sys.stdin.readline


def check_row(rn,rcheck):
    row0 = [sudoku[(rn//9)*9+i] for i in range(9)]
    
    return rcheck not in row0

def check_col(cn,ccheck):
    col0 = [sudoku[(cn%9)+i*9] for i in range(9)]
    return ccheck not in col0

def check_box(bn,bcheck,m):
    box0 = [sudoku[i] for i in box[zero_squ[m]]]
    return bcheck not in box0

def bk(m,sudoku):
    if m == len(zero):
        print('s',s)
        return s
    
    for i in candidate[m]:
        if check_row(zero[m],i) and check_col(zero[m],i) and check_box(zero[m],i,m):

            sudoku[zero[m]] = i 
            bk(m+1,sudoku)
            sudoku[zero[m]] = 0
        
sudoku = []
for i in range(9):
    sudoku += list(map(int,input().split()))
# print(sudoku)



zero = []
for i in range(81):
    if not sudoku[i]: zero.append(i)
        
visited = [False for i in range(len(zero))]

start_n = sorted([ i+27*j for i in [0,3,6] for j in range(3)])
plus_n = [9*i+j for i in range(3) for j in range(3)]
box = [[i+j for j in plus_n] for i in start_n]

zero_squ = []
num_cnt = [sudoku.count(i) for i in range(10)]


for i in zero:
    for n_in in range(9):
        if i in box[n_in]: zero_squ.append(n_in); break
            
zero_check = [[] for i in range(len(zero))]
for i in range(len(zero)):
    for j in range(i+1,len(zero)):
        if zero[i]//9 == zero[j]//9 or zero[i]%9 == zero[j]%9 or zero_squ[i] == zero_squ[j]:
            zero_check[i].append(zero[j])
            zero_check[j].append(zero[i])
            
candidate = [[] for i in range(len(zero))]
for z_idx in range(len(zero)):
    n = zero[z_idx]

    row = [(n//9)*9+i for i in range(9)]
    col = [(n%9)+i*9 for i in range(9)]

    now = set([ sudoku[i] for i in set(row+col+box[zero_squ[z_idx]])])
    for i in range(10):
        if i not in now and i != 0:
            candidate[z_idx].append(i)
        # print(i,candidate[z_idx])

    
def bk(m,sudoku):
    if m == len(zero):
        for k in range(9):
            print(*sudoku[0+9*k:9+9*k])
        quit()
        return 
    
    for i in candidate[m]:
        if check_row(zero[m],i) and check_col(zero[m],i) and check_box(zero[m],i,m):

            sudoku[zero[m]] = i 
            bk(m+1,sudoku)
            sudoku[zero[m]] = 0

s = []
bk(0,sudoku)