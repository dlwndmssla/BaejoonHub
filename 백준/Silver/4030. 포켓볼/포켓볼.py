import math

def find_case(a, b):
    ans = 0
    a1 = math.floor(math.sqrt(a))   
    b1 = math.ceil(math.sqrt(b))   
    
    for n in range(a1, b1 + 1):
        X = n**2-1
        if not (a < X+1 < b):
            continue
        
        m = pow(2*n**2-7/4,0.5)-0.5
        # n이 완전제곱수인지 확인

        if m == int(m):
            #print(pow(2*n**2-7/4,0.5)-0.5)
            ans += 1

    return ans

cnt = 0
while True:
    cnt += 1
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    print(f"Case {cnt}: {find_case(a, b)}")
