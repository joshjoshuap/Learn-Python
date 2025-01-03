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