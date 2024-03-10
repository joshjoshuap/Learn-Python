# --- DATA TYPES ---
number = 1
float = 5.5
string = 'Joshua'
StringList = ['Apple', 'Banana', 'Orange']
NumberList = [1,2,3]
Tuples = (1,2,3)
CombinedList = ['one', 2, 'three']
Dictionaries = {'firstname' : 'Joshua', 'age': 24}
isTrue = True

# --- ARITHMETIC ---
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

# --- LISTS ---
firstLists = [1,2,3]
secondLists =[5,6,7]
combinedLists = firstLists + secondLists
randomNumberLists = [2,1,4,7,6,8]

firstLists[0] = 'One'
secondLists.pop() # [5, 6] 
secondLists.append(8)  # [5, 6, 8] 
randomNumberLists.sort() # sorting list
sortedList = randomNumberLists # calling the sorted list

# print(combinedLists) # [1, 2, 3, 5, 6, 7]
# print(firstLists) # ['One', 2, 3]
# print(secondLists)
# print(sortedList) # [1, 2, 4, 6, 7, 8]

# --- DICTIONARIES / OBJECTS ---
userInfo = {'name' : 'Jose', 'age' : 100, 'address' : 'Quezon City', 
            'grades' : {'quiz1' : 100, 'quiz2' : 80}
    }

userInfo['grades']['quiz1'] = 74

# print(userInfo['name']) # Jose
# print(userInfo['grades']['quiz2']) # 80
# print(userInfo['grades']['quiz1']) # 74

# --- TUPLES ---
numberTuples = (1,2,3)
sampleNumberLists = [1,2,3]

sampleNumberLists[0] = 'One'
# numberTuples[0] = 'one' # error, tuples can't change value

# print(sampleNumberLists)
# print(numberTuples) # error, tuples can't change value

# --- SET ---
listOfNumbers = [1,1,1,2,3,3,4,5,6,6,6,7,7,8,9,9,9]
newSet = set(listOfNumbers) # remove repeatedly value in lists

print(newSet)
