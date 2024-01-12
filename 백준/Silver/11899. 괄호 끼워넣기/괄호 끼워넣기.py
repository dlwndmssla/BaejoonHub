ex = str(input())
while '()' in ex:
    ex = ex.replace('()', '')
print(len(ex))