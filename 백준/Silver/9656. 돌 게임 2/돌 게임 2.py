n = int(input())
print(['CY','SK'][(int(n/3)+n%3)%2 == 0])