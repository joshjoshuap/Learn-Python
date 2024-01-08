age = 19
if age <= 2:
    print('Hello Baby')
elif age > 2 and age <= 12:
    print('Hello Kid')
elif age > 12 and age <= 18:
    print('Hey Teenager')
elif age > 18 and age <= 60:
    print('Sir/Mam')
elif age > 60:
    print('Veteran')
else:
    print('Enter valid age only')