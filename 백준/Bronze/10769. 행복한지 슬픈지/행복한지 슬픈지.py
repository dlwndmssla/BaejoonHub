ex = str(input())

sad = 0
happy = 0
for i in range(len(ex)-3): 
    if ex[i:i+3] == ':-(':
        sad+=1
    if ex[i:i+3] == ':-)':
        happy+=1

if sad+happy ==0:
    print('none')
elif sad==happy:
    print('unsure')
elif sad>happy:
    print('sad')
else:
    print('happy')