# Try except Handling

# try:
#     age = int(input('Enter your age: '))
#     print(age)
# except:
#     print('Please enter valid age!!!!') 
    
    
# Try except using Loop

while True:
    try: 
        userAge= int(input('What is your age? '))
        10/userAge
    except ValueError:
        print('Please enter value age')
        continue
    except ZeroDivisionError:
        print('Enter age higher than 0')
        break
    else:
        break
