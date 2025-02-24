
def check_c(sqr3,sqr4):
    c1 = sqr3[1] == sqr4[0]
    c2 = sqr3[0] == sqr4[1]
    c3 = [sqr3[0][1],sqr3[1][0]] == [sqr4[1][0],sqr4[0][1]]
    c4 = [sqr3[1][0],sqr3[0][1]] == [sqr4[0][0],sqr4[1][1]]
    return 1 == sum([c1,c2,c3,c4])   

def check_d1(sqr3,sqr4):
    d_y = max(sqr3[0][0],sqr3[1][0])<min(sqr4[0][0],sqr4[1][0])
    d_x = max(sqr3[0][1],sqr3[1][1])<min(sqr4[0][1],sqr4[1][1])
    return d_y or d_x

def check_d(sqr1,sqr2):
    return check_d1(sqr1,sqr2) or check_d1(sqr2,sqr1) 


def check_b(sqr3,sqr4,d,c):
    b_1 = sqr3[1][0] == sqr4[0][0]
    b_2 = sqr3[1][1] == sqr4[0][1]
    return (b_1 + b_2 == 1) and (not (d or c))

def check_a(b,c,d):
    return not (b or c or d)

def check(node_list):
    sqr = []
    for y,x in zip(node_list[::2],node_list[1::2]):
        sqr.append((y,x))
    sqr1,sqr2 = sqr[:2],sqr[2:]
    d = check_d(sqr1,sqr2)
    c = check_c(sqr1,sqr2)
    b = check_b(sqr1,sqr2,d,c) or check_b(sqr2,sqr1,d,c)
    a = check_a(b,c,d)
    # print(a,b,c,d)
    if a:print('a')
    elif b:print('b')
    elif c:print('c')
    else :print('d')




for i in range(4):
    node_list = list(map(int,input().split()))
    check(node_list)
