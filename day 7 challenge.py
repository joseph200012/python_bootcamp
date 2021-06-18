# 1.	Create a function getting two integer inputs from user & print the following:

def function1(x,y):
	#addition
	print('Addition of two number is ' + str(int(x)+int(y)))
	#Subraction
	print('Subtraction of two number is ' + str(int(x) - int(y)))
	#Division
	print('Division of two number is ' + str(int(x) / int(y)))
	#Multiplication
	print('Multiplication of two number is ' + str(int(x) * int(y)))
function1(x=int(input("enter the first number :")), y=int(input("enter the second number :")))


# Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree

def covid(patient_name, body_temperature):
	print("Patient's Details: ")
	print("Patient's name : " + patient_name)
	print("Default temperature : 98 degree " + " Patient's body temperature : " + str(body_temperature) + " degree" )
covid(patient_name=str(input("Enter the Patient's name : ")), body_temperature=int(input("Enter the Patient's body temperature in degree : ")))


