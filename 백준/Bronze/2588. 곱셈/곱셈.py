num1 = int(input())
num2 = str(input())
num2_list = [int(i) for i in num2]
a = [i*num1 for u,i in enumerate(num2_list[::-1])]
for i in a: print(i)
print(num1*int(num2))
