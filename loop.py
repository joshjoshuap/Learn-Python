numberLists = [1,2,3,4,5,6,7,8,9]

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
number = 10;
for num in range(1, number+1):
    print('range', num)

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
    
# FizBuzz
target = 100
for number in range (1, target+1):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number);

