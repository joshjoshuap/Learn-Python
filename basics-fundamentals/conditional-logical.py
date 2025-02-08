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
# number = int(input("Input a number: ")) 
# if number % 2 == 0:
#     print("Number is Even")   
# elif number % 1 == 0:
#     print("Number is ODD")
    
# Logical
userAge = 18
userLicensed = True

if userAge >= 18 and userLicensed == True:
    print('You are allowed to driver')
elif userAge >= 18 and userLicensed == False:
    print('You need a driver license first')
elif userAge <= 18 and userLicensed == True:
    print("You're driver license is invalid, cause your a minor")
else:
    print('You are not allowed to take license and drive')
    
# Tenary Operator
userAge2 = 16 
userLicensed2 = True
if userAge2 >= 18 and userLicensed == True: print('You are allowed to driver')
if userAge2 <= 18 and userLicensed == True: print("You're driver license is invalid, cause your a minor")
if userAge2 >= 18 and userLicensed == False: print('You need a driver license first')
if userAge2 <= 18 and userLicensed == False: print('You are not allowed to take license and drive')

