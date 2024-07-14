n = int(input())

list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
list1.sort()
list2.sort(reverse=True)

print( sum( list1[i]*list2[i] for i in range(n)))