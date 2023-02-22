from string import ascii_lowercase
exam = list(ascii_lowercase)

m = input()

if m.isnumeric() == True:
    print(48+int(m))
elif m.isupper() == True:

    for i in range(len(exam)):
        if exam[i] == str(m.lower()):
            print(i + 65)
else:
    for i in range(len(exam)):
        if exam[i] == str(m):
            print(i + 97)