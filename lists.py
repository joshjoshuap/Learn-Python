# LISTS
firstLists = [1,2,3]
secondLists =[5,6,7]
stringList = ['a', 'b', 'c', 'd', 'e', 'e', 'e']
combinedLists = firstLists + secondLists
randomNumberLists = [2,1,4,7,6,8]

# firstLists[0] = 'One' # ['One', 2, 3]

# removing
secondLists.pop() # [5, 6] 
secondLists.append(8)  # [5, 6, 8] 

# adding
secondLists.insert(0, 4) # [4, 5, 6, 8]
secondLists.extend([9, 10]) # [4, 5, 6, 8, 9, 10]

# sorting
# randomNumberLists.sort() # [1, 2, 4, 6, 7, 8]
randomNumberLists.reverse() # [8, 6, 7, 4, 1, 2]
sortedList = randomNumberLists # calling the sorted list

# unpacking
one,two,three = [1, 2, 3]
print(two) # 2

# methods
# print(stringList.index('c')) # 2
# print(stringList.count('e')) # 3
# print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(combinedLists) # [1, 2, 3, 5, 6, 7]
# print(firstLists) 
# print(secondLists)
# print(stringList)
# print(sortedList) 

# NESTED LISTS / MULTIPLE LIST
nestedlist = [firstLists, secondLists]
# print(nestedlist) #[['One', 2, 3], [5, 6, 8]]
# print(nestedlist[0][0]) # One
