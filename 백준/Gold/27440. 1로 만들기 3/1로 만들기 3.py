from collections import deque
n = int(input())

c_dict = {n:0}
queue = deque()
queue.append(n)
while queue:
    num = queue.popleft()
    now = c_dict.get(num)
    for i in [3,2,1]:
        if [0, num <=1, num%2, num%3][i]: continue
        mod_i = [0,num-1,num//2,num//3][i]
        now_i = c_dict.get(mod_i,n)
        # print(i,now_i,now+1)
        if now_i > now+1:
            queue.append(mod_i)  
            c_dict[mod_i] = now+1
        if c_dict.get(1,n) != n:
            queue = deque()
            
print(c_dict[1])
