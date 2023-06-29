# Notes

print("Hello world")

# 4 variable(string, integer, float, boolean)
name = "air"  # string
age = 45   # integer
# variable can be changed
name = "sir"  # string
age = 12.5   # float
print(name)  # print Function
print(age)
is_he_adult = True  # boolean(True / False)
print(is_he_adult)
# inisilizing of variable is not required


# Exercise

firstname = "Tony"
lastname= "Stark"
age = 51
is_genius = True


name = input("what is ur name ?")  # input Function
print (name + " is a human")  # "+" for concatination
# concatination is possible in string type variable only


# Exercise
superhero = input("what is the name of ur superhero")
print(superhero)


# type conversion
old_age = input("enter ur old age")
new_age= int(old_age) + 2
print(new_age)

# int() for integer
# float() for float
# str() for string
# bool() for boolean


first = int(input("enter fisrt no"))
second = int(input("enter second no"))
sum = first + second
print(sum)
print("the sum is " ,sum)
print("the sum is " + str(sum))  # converting int(sum) into str because concatination can not done between string & integer


# string operation
name = "tony stark"
print(name.upper()) # upper() for upper case
# lower() for l case
# find('a')   it find the index of string in the variable. Index start from 0, if index return "-1" then that string or charater is not present in the string , it is case sensitive
# replace("tony stark", "ironman")   replace existing substring or string or charater to new string
# keyword :- dictionary in python
print('T' in name)  # for checking whether a charater or a string is present in the variable and give output as true or false. It is case sensitive
# "in" is a keyword
# "print, input" are keywords
# These string operation doesn't affect the main variable.


# arithmetic operators
print(2+5)
# "+" for sum
# "-" for subtract
# "*" for multipy
# "/" for divide
# "//" for divide but it dont include the decimal value in output as 5/2=2.5 but 5//2= 2
# "%" for remainder (modulo)
# "**" for power


# Shortcuts
i = 5
i= i+2
i += 2 # it is minimized form of above equation(i= i+2)
# Similarlity "-=, *="


# operator precedence


# Comments
# it is used by using the symbol"#"



# Comparsation operator
print (2 > 3)
# it return boolean values
# ">"  for greater than
# "<" for less than
# ">="  for greater than and equal
# "<=" for less than and equal
# "==" for comparsition between two numbers
# "!" symbolize not
# "!=" for not equal


# Logical operator
print(2 > 3 or 2 > 1)
# "or" if we give two condition, then atleast one is true then it give true or it gives false
# "and"  if we give two condition,then the both condition are true then it give true or else false
print(not 2 > 3 )
# "not" it make true false and make false true


# if-else statement
age = 19
if age >= 18:  # below line (115, 116) will print when the condition is true
    print("you are an adult")
    print("you can vote")
elif age < 18 and age > 18:
    print("you are in school")
else:
    print("u r a child")


# Mini project
first = int(input("enter first number"))
second = int(input("enterr second number"))
operator = input("enter operator(+,-,*,/)")

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("invaild operator")


# Range
number = range(5)  #0, 1, 2, 3, 4
print(number)


# Loop
i = 1
while i <= 5:
    print(i)  # without below condition it will infinite loop where the output will be continously printing "1"
    i= i+1

i = 1
while i <= 5:
        print(i * "*")   #here "* " it multipy the given symbol or charater or word by the number "i"
        i = i + 1
# for reverse
i = 5
while i >= 0:
        print(i * "*")
        i = i - 1


# For loop
for i in range(5):
    print(i)


# string Float integer boolean are primitive datatype

# List data type "[]"
# we can store primitive datatype in list
# it is collection of item
marks = [95, 98, 97, "maths"]
print(marks)
print(marks[0])  # print by index as "[]" {0, 1, 2 & -3, -2, -1}
print(marks[0:2])   # by starting index to ending index but it dont include ending element


# loop in list
marks = [95 , 68, 97]

# loop by using forloop
for score in marks:
    print(score)

# append operation
marks = [95, 68, 97]
marks.append(99)
print(marks)

# insert operation
marks = [95, 68, 97]
marks.insert(0, 99)  # here "0" is the index and "99" is the value
print(marks)

# to check
marks = [95, 68, 97]
marks.insert(0, 99)
print(marks in marks)  # to check the existing element

# length operation
marks = [95, 68, 97]
print(len(marks))

# loop by using while
marks =[95, 98, 97]
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

# clear operation
marks = [95, 68, 97]
marks.clear()
print(marks)


# Break & Continue
#break
student = ["ram", "shyam", "kishan", "radha", "raj"]
for student in student:
    if student == "radha":
        break;
    print(student)
# Continue
student = ["ram", "shyam", "kishan", "radha", "raj"]
for student in student:
    if student == "kishan":
        continue;
    print(student)


# tuple "()"
#tuple is immutable
marks= (95, 96, 97, 97, 97)
#marks[0] = 99   #error it doesnt support item assignmnet
#count
print(marks.count(97))
#index
print(marks.index(97))

person = "ram", "kam", "raj"  #this is also a tuple
print(person)


# Set "{}"
# for unique element
marks= {95, 96, 97, 97, 97}
print(marks)  #output : 95, 96, 97
# no multiple elements
print(marks[0])  #error
# there is no index in set
# it is unordered


# Dictionary
# store key value pair
marks= {"english" : 95, "chemistry": 96}
print(marks["chemistry"])
marks["physics"] = 97;
print(marks)

marks["physics"] = 99;
print(marks)


# Function
# 1. in-built Function
# int()
# str()
# bool()

# 2. Module Function
import math
print(dir(math))  # print function of math module

from math import sqrt
print(sqrt(16))

# 3. User-Defined Function
# del function_name(parameters):
  # //do something

def print_sum(first, second):
    print(first + second)
print_sum(1, 2)

def print_sum(first, second = 4):
    print(first + second)
print_sum(1)
