numberLists = [1,2,3,4,5,6,7,8,9]
alphabetList = ['a', 'b', 'c', 'd']

# WHILE
x = 0
while x <= 5:
    print(x)
    x += 1

# FOR LOOP
for num in numberLists:
    print(num)

# FOR IF ELSE 
for evenNumber in numberLists:
    if evenNumber % 2 == 0:
        print(evenNumber) 

# For in Range
for num in range(6):
    print('range', num + 1)
    
# Nested Looping
for num in numberLists:
    for letter in alphabetList:
        print(num, letter)

# ADDING BY LOOPING
addNumbers = 0
for number in numberLists:
    addNumbers = addNumbers + number
print(addNumbers) # 45

# TUPLE LOOPING
myListTuple = [(1,2), (3,4), (5,6)]
for a,b in myListTuple:
    print (a) # only display the first index of tuple
    print (a,b)
    print (b)
    
# Dictionaries
userProfile = {
    'name': 'Joshua',
    'age': 24,
    'city': 'Quezon City'
}

for key, value in userProfile.items():
    print(f'{key} {value}')
    # name Joshua
    # age 24
    # city Quezon City
    
for item in userProfile.values():
    print(item)
    # Joshua
    # 24
    # Quezon City 
 
for item in userProfile.keys():
    print(item)    
    # name
    # age
    # city
    
# FizBuzz
target = 100
for number in range (1, target+1):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number);

