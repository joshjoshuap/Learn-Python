# --- STRING INDEXING / SLICING ---
indexingString = "Hello World"
slicingString = "Josh Joshua"
stepSlicingString = '123456789'

# print(indexingString[0]) # first letter
# print(indexingString[-1]) # last letter
# print(slicingString[5:]) # Joshua
# print(slicingString[0:4]) # Josh
# print(stepSlicingString[::2]) # 13579
# print(stepSlicingString[0:5:2]) # 135

# --- STRING METHODS ---
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

# --- STRING FORMATTING ---
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