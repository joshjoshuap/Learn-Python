# DICTIONARIES / OBJECTS

# Single Dictionaries
userInfo = {'name' : 'Jose', 'age' : 100, 'address' : 'Quezon City', 'grades' : {'quiz1' : 100, 'quiz2' : 80}
    }
userInfo['grades']['quiz1'] = 74\
    
# print(userInfo['name']) # Jose
# print(userInfo['grades']['quiz2']) # 80
# print(userInfo['grades']['quiz1']) # 74

# Multiple Dictionaries
userInfo2 = [ 
    {'name': 'Joshua', 'age': 25}, 
    {'name': 'Jose', 'age': 25}
    ]
   

# print(userInfo2[1]['name']) # Jose

# Methods
userInfo3 = {'name': 'Maria', 'address' : 'Quezon City', }
new_info = userInfo3.get('age', 0) # adding default value 0 in age keys
# print(new_info) # 0
 
userInfo_copy = userInfo3.copy() # copy dictionary
# print(userInfo_copy)

userInfo3.pop('address') # {'name': 'Maria'} 
print(userInfo3)
