# IF Else
age = 2
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
    
# Odd / Even
number = int(input("Input a number: ")) 
if number % 2 == 0:
    print("Number is Even")   
elif number % 1 == 0:
    print("Number is ODD")