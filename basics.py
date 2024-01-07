# DATA TYPES
number = 1
float = 5.5
string = 'Joshua'
StringList = ['Apple', 'Banana', 'Orange']
NumberList = [1,2,3]
CombinedList = ['one', 2, 'three']
Dictionaries = {'firstname' : 'Joshua', 'age': 24}
isTrue = True

# ARITHMETIC
number1 = 5
number2 = 8
number3 = 10

addition = number1 + number2
subtraction = number2 - number3
multiplication = number1 * number2 * number3
division = number3 / number1
modulo = number2 % number3
remainder = 23 % 2 
noRemainder = 22 % 2 
power = 2 ** 3 
multiples = 2 + 3 * 4 + 5 
specifics = (2 + 3) * (4 + 5) 

# print(remainder) # 1
# print(noRemainder) # 0
# print(power) # 2 * 2 * 2 = 8
# print(multiples) # 19
# print(specifics) # 45

# STRING INDEXING / SLICING
indexingString = "Hello World"
slicingString = "Josh Joshua"
stepSlicingString = '123456789'

# print(indexingString[0]) # first letter
# print(indexingString[-1]) # last letter
# print(slicingString[5:]) # Joshua
# print(slicingString[0:4]) # Josh
# print(stepSlicingString[::2]) # 13579
# print(stepSlicingString[0:5:2]) # 135

# STRING METHODS
firstName = 'Joshua'
lastname = 'Pautanes'
helloWorld = 'Hello World'
multipleLetter = 'J' * 10

stringConcat = firstName + ' ' + lastname
lowerCase = firstName.lower()
upperCase = lastname.upper()
stringLength = len(firstName)
splitString = helloWorld.split();

# print(stringLength) # 6
# print(stringConcat) # Joshua Pautanes
# print(multipleLetter) # JJJJJJJJJJ
# print(lowerCase) # joshua
# print(upperCase) # PAUTANES
# print(splitString) # ['Hello', 'World']

# String Formatting
name = 'Joshua'
age = 23
address = 'Quezon City'
pi = 3.14159265359

introduction = 'My name is {} {} years old from {}'.format(name, age, address)
introduction2 = 'My name is {name} from {address} and {age} years old'.format(name = 'Jose', age = 99, address = 'Manila')
shortenedPI = 'The PI is {total:1.3f}'.format(total=pi)

# print(introduction) # My name is Joshua 23 years old from Quezon City
# print(introduction2) # My name is Jose from Manila and 99 years old
# print(shortenedPI) # The PI is 3.142