# Basics
def sample_Function():
    firstName = "Joshua"
    lastName = "P"
    print(f'{firstName} {lastName}')

sample_Function()

# Calling Functions
def num1():
    num1 = 5
    return num1

def num2():
    num2 = 10
    return num2

def addNumbers():
    total = num1() + num2()
    return total

print(addNumbers())

# Nested Function
def inputNumber(num1, num2):
    def sum(num1, num2):
        return num1 + num2
    return sum(num1, num2)

total = inputNumber(10, 100)
print(total)

# Paramaters Values
def name(inputName):
    print(f"Hello {inputName}")
    
# userInput = input("What is your name? ")
# name(userInput)

# Default Value
def userProfile(name,age = 0):
    print(f'Name: {name} Age: {age}')
    
name = 'Joshua'    
# age = 24
userProfile(name,)

# Docstrings
def unknownFunction(test):
    '''
    >>> This is the function that print
    '''
    print(test)
    
unknownFunction('Hello')
print(unknownFunction.__doc__)