

#explain python syntax 
x = "Python Syntax"

a= " refers to the set of rules and conventions that dictate how Python code should be written and structured."
b= "Indentation: Uses indentation to define code blocks."
c= "Comments: Start with # and are ignored by the interpreter."
d= "Variables: No need to declare types, just assign values."
e = "Data Types: Include integers, floats, strings, lists, tuples, dictionaries, sets."
f = "Control Structures: If statements, loops (for, while), try-except blocks."
g = "Functions: Defined with def keyword."
h = "Classes: Defined with class keyword."
i = "Modules and Packages: Used for organizing code into reusable components."

print("What is Python Syntax?")
print(x + a)
print("It has some key points which are:")
print(b)
print(c)
print(d)
print(e) 
print(f)
print(g)
print(h)
print(i)
print("---------------------------")


#this is a comment
print('Hello World!')
print("---------------------------")


#python variables
x = "Kobe Bryant"
y = 24
print(x)
print(y)
print("---------------------------")


#Variable Names
myplayer = "Lebron James"
MYplayer = "Lebron James"
_myPlayer = "Lebron James"
my_PLAYER = "Lebron James"
_my_player = "Lebron James"
my_player2 = "Lebron James"
print(myplayer)
print(MYplayer)
print(_myPlayer)  
print(my_PLAYER)
print(_my_player)
print(my_player2)
print("---------------------------")


#Multiple values
player1, player2, player3 = "Kobe Bryant", "Michael Jordan","Lebron James"
print(player1)
print(player2)
print(player3)
print("---------------------------")


#Output variables
player1 = "This is the Legendary Kobe Bryant, a 5 time NBA Champion and NBA Hall of Famer."
player2 = "Stephen Curry is the greatest shooter of all time."
player3 = "Mugsy Bouges is the smallest NBA player of all time."
print(player1, player2, player3)
print("---------------------------")


#Global Variables
player1 = "Greatest Rebounder of Alltime."

def function():
  global player1
  player1 = "The Greatest Shooter of Alltime."

function()

print("Stephen Curry is " + player1)
print("---------------------------")
#display name
name = input("What is your name?: ")

print("Hello! My name is " + name +".")
print("---------------------------")

#display name with global variables
name = "Joemari G. Esguerra"

def function():
  print("My complete name is " + name + ".")
function()
print("---------------------------")

#adding 2 numbers

num1 = int(input("1st Number: "))
num2 = int(input("2nd Number: "))
sum = int(num1 + num2)

print("The sum is: ") 
print(sum)
print("---------------------------")

#Simple Calculator
print("---------------------------")
print("THIS IS A SIMPLE CALCULATOR")
print("---------------------------")
print("Select operation to perform. Choose from numbers 1 to 4.")
print("---------------------------")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("---------------------------")
print("---------------------------")

option = input()

if option == '1':
  print("You chose ADDITION!")
  num1 = input ("Enter 1st number: ")
  num2 = input ("Enter 2nd number: ")
  print("The sum is " + str(int(num1) + int(num2)))
  print("Thank you for using my calculator!")
  print("---------------------------")
elif option == '2':
  print("You chose SUBTRACTION!")
  num1 = input ("Enter 1st number: ")
  num2 = input ("Enter 2nd number: ")
  print("The difference is " + str(int(num1) - int(num2)))
  print("Thank you for using my calculator!")
  print("---------------------------")
elif option == '3':
  print("You chose MULTIPLICATION!")
  num1 = input ("Enter 1st number: ")
  num2 = input ("Enter 2nd number: ")
  print("The product is " + str(int(num1) * int(num2)))
  print("Thank you for using my calculator!")
  print("---------------------------")
elif option == '4':
  print("You chose DIVISION!")
  num1 = input ("Enter 1st number: ")
  num2 = input ("Enter 2nd number: ")
  print("The qoutient is " + str(int(num1) / int(num2)))
  
  print("---------------------------")
else:
  print("You chose an invalid number.")
print("---------------------------")