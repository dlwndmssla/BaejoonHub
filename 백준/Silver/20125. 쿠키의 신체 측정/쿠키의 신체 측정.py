def check_heart(cookie):        
    for i,r in enumerate(cookie):
        if r.count('*') == 1:
            return [i+1,r.index('*')]

def check_arms(cookie,heart):
    # print(cookie[heart[0]])
    arm_s = cookie[heart[0]].index('*')
    arm_e = arm_s+cookie[heart[0]].count('*')

    # print(arm_s,heart[1],arm_e)
    return [heart[1]-arm_s,arm_e-heart[1]-1]
    
def check_waist(cookie,heart):
    return [int(cookie.count(cookie[heart[0]-1])-1)]

def check_legs(cookie,heart,waist):    
    leg_lengths = []
    trans_legs = [list(i) for i in zip(*cookie[heart[0]+waist[0]+1:][::-1])]
    for leg in trans_legs:
        leg_length = leg.count('*')
        if not leg_length: continue
        leg_lengths.append(leg_length)
        
    return leg_lengths

        
n = int(input())

cookie = [str(input()) for i in range(n)]
# print(cookie)

heart = check_heart(cookie)
arms = check_arms(cookie,heart)
waist = check_waist(cookie,heart)
legs = check_legs(cookie,heart,waist)
body = arms+waist+legs
print(heart[0]+1,heart[1]+1)
print(*body)
