exam = list(map(int, input().split()))
list1 = 0
for i in range(8):
    if exam[i] == i+1:
        list1 +=1
    elif exam[i] == 8-i:
        list1 +=2
    else:
        list1 +=0     
if list1 == 8:
    print("ascending")
elif list1 == 16:
    print("descending")
else:
    print("mixed")