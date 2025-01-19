# SET
listOfNumbers = [1,1,1,2,3,3,4,5,6,6,6,7,7,8]
newSet = set(listOfNumbers) # remove repeatedly value in lists
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(newSet) 

# methods
firstSet = {1,2,3,4,5}
secondSet = {4,5,6,7,8,9}
print(firstSet & secondSet) # {4,5}
print(firstSet | secondSet) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
