#Write a Python program for all the cases which can check a string contains only a certain set of characters 
import re

def is__specific__char(string):
    charre = re.compile(r'[^a-zA-Z0-9.]') 
    string = charre.search(string) 
    return not bool(string)
    
print(is__specific__char("Joseph2000")) 
print(is__specific__char("1373@₹#&%$"))

#Write a Python program that matches a word containing 'ab'. 

def word_match(word):
        patterns = '\w*ab.\w*'
        if re.search(patterns,  word):
                return ('Found a match!')
        else:
                return('Not matched!')

print(word_match("abkhjab"))
print(word_match("python bootcamp"))

#Write a Python program to check for a number at the end of a word/sentence.

def Endnum(string):
    word= re.compile(r".*[0-9]$")
    if word.match(string):
        return True
    else:
        return False

print(Endnum('ghrj'))
print(Endnum('ghsh59667'))
print(Endnum('flhhs6886'))

#Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

res = re.finditer(r"([0-9]{1,3})", "Exercises number 2, 8, 11, and 111are important")
print("Number of length 1 to 3")
for n in res:
    print(n.group()) 
    
   
#Write a Python program to match a string that contains only uppercase letters

def word_match(word):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  word):
                return( 'Found a match!')
        else:
                return('Not matched!')

print(word_match("This is joseph."))
print(word_match("Python_Bootcamp"))