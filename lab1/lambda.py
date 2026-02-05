n = input()
fact = True
for i in n:
    if int(i) % 2 !=0:
        fact = False
        break
if fact:
    print("Valid")
else:
    print("Not valid")