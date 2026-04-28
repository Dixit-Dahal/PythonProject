age = 50

print(id(age))

EmptyDict = {}    # Empty Dictionary

EmptySet = {*()} # Empty Set

EmptyTuple = tuple()    # Empty Tuple
EmptyTuple2 = ()

print("Dixit\tRabeen")

# String Methods

student_results = ['A+','B+','A+']
print(len(student_results))             # Used to get the length of all items
print(student_results.count('A+'))      # Used to get the count of specific item/items

print('ram'.maketrans('r', 'R'))        # maketrans() method is used to transform a character within a string

num1 = 30
num2 = 40

print('The total sum of {0} and {1} is {result}'.format(num1, num2, result = num1+num2))
print(F'The total sum of {num1} and {num2} is {num1+num2}')

name = "Ram"
corrected_data = name.replace('r', 'R') # Replaces r with R; Checks data sequentially
print(corrected_data)
corrected_data = name.maketrans('rd','RM') # Stores ASCII value in corrected_data
print(corrected_data) # Prints ASCII Value

# To print the actual data
print(name.translate(corrected_data)) # Since there is no d in the actual data, only the r will be corrected and printed


first_name = 'ram'
middle_name = 'bahadur'
last_name = 'kc'

print(first_name + '_' + middle_name + '_' + last_name) # Works for strings data type only

print(first_name, middle_name, last_name, sep = '_') # Works for every value, the default value of sep is " "

print('_'.join((first_name, middle_name, last_name))) # Works only with tuples, dictionary, list or set as it accepts single argument

items = [first_name, middle_name, last_name] # used a list
print('_'.join(items))

print(f'{first_name}_{middle_name}_{last_name}') # Works using f string as well

print(first_name.center(13)) # Adds space to both sides according to the length of the attribute
print(first_name.center(13, '*')) # Adds * instead of space to both sides

# Here, length of first_name is 3 which is odd

# for odd lengths, left = (n-1)/2; right = (n+1)/2; where n = x - len(first_name); x = center(x)
# for even lengths, left = (n+1)/2; right = (n-1)/2; 
# Again, this works only when n = odd