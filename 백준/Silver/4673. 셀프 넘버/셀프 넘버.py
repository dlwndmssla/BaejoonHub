
self_num_dict = set()
def d(num): return num+sum([ int(i) for i in str(num)])
    

for i in range(1, 10000+1):
    self_num_dict.add(d(i))
    if i not in self_num_dict:
        print(i)