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

# Passing Values
def name(inputName):
    print(f"Hello {inputName}")
    
userInput = input("What is your name? ")
name(userInput)
