#assign multiple objects to same value

a = b = c = 20
print(a/10)
print(b*50)
print(c+60)

#using replace to make changes in string variable

City = "DEHRI"
print(City.replace("H", "G"))

#create two variables and convert them into int and float

a,b=5,3.8
print('a=',a,'b=',b)
print('data type of a :',type(a))
print('data type of b :',type(b))
a=float(a)
b=int(b)
print('value of a and b after type converstion:')
print('a=',a,'b=',b)
print('data type of a after type conversion:',type(a))
print('data type of b after type conversion:',type(b))

