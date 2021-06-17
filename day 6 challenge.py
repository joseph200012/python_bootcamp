#write a python script to merge two python dictionaries 
def merge(dict1, dict2): 
       res= {**dict1, **dict2 }
       return res 
dict1={"j":1, "l":2} 
dict2={"h":3, "f":4} 
dict3= merge(dict1,dict2)
print(dict3)

#write a python program to remove a key from dictionaries 
dict4={"raju":75, "dannish":70, "louis":60, "babu":95} 
print("Dictionaries before removal :", dict4) 
del dict4["babu"] 
print("Dictionaries after removal :",dict4)

#write a python program to map two list into a dictionaries 
keys=['beetroot','tomato','onion','carrot'] 
value=['60','85','20','120'] 
vegetables=dict(zip(keys,value)) 
print(" mapping two list into dictionaries :",vegetables)

#write a python program to find the length of the set 
j =len({"11","31","32","83","74"})
print("The length of the set is :",j)

#writs a python program to remove the intersection of 2nd set from 1st set 
set1={'1','2','3','4','5'} 
set2={'5','7','2','9','1'} 
print("Current set :") 
print(set1) 
print(set2) 
print("\n remove the intersection of 2nd set from 1 st set using -= operator :") 
set1 -= set2 
print("set1",set1) 
print("set2",set2)
