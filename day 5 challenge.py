# to create a list and to add, delete, find max , min etc
print('Write a program to create a list of n integer values and do the following:')

a = []

for i in range(0,51):
	a.append(i)
print(a)

#Add an item in to the list (using function)
print('Add an item in to the list (using function):')
a.append(51)

#Delete (using function)
print('Delete (using function):')
del a[15]

print(a)

#Store the largest number from the list to a variable
print('Store the largest number from the list to a variable:')
max_in_the_list = max(a)
print(max_in_the_list)

#Store the Smallest number from the list to a variable
print('Store the Smallest number from the list to a variable:')
min_in_the_list = min(a)
print(min_in_the_list)

# 2) Create a tuple and print the reverse of the created tuple
print('Create a tuple and print the reverse of the created tuple:')
tuple1 = (11,12,13,14,15)
print(tuple1)
reversedTuple1 = reversed(tuple1)
print(tuple(reversedTuple1))

#  3) Create a tuple and convert tuple into list
print('Create a tuple and convert tuple into list:')
tuple2 = (16,17,18,19,20)
print(tuple2)
list_tuple = list(tuple2)
print(list_tuple)
