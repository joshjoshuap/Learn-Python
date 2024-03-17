# LISTS
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

# NESTED LISTS / MULTIPLE LIST
nestedlist = [firstLists, secondLists]
print(nestedlist) #[['One', 2, 3], [5, 6, 8]]
print(nestedlist[0][0]) # One

# DICTIONARIES / OBJECTS
userInfo = {'name' : 'Jose', 'age' : 100, 'address' : 'Quezon City', 'grades' : {'quiz1' : 100, 'quiz2' : 80}
    }
userInfo['grades']['quiz1'] = 74

# print(userInfo['name']) # Jose
# print(userInfo['grades']['quiz2']) # 80
# print(userInfo['grades']['quiz1']) # 74

# TUPLES 
numberTuples = (1,2,3)
sampleNumberLists = [1,2,3]

sampleNumberLists[0] = 'One'
# numberTuples[0] = 'one' # error, tuples can't change value

# print(sampleNumberLists)
# print(numberTuples) # error, tuples can't change value

# SET
listOfNumbers = [1,1,1,2,3,3,4,5,6,6,6,7,7,8,9,9,9]
newSet = set(listOfNumbers) # remove repeatedly value in lists

print(newSet)