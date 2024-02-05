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


#this is a comment
print('Hello World!')


#python variables
x = "Kobe Bryant"
y = 24
print(x)
print(y)


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


#Multiple values
player1, player2, player3 = "Kobe Bryant", "Michael Jordan","Lebron James"
print(player1)
print(player2)
print(player3)

#Output variables
player1 = "This is the Legendary Kobe Bryant, a 5 time NBA Champion and NBA Hall of Famer."
player2 = "Stephen Curry is the greatest shooter of all time."
player3 = "Mugsy Bouges is the smallest NBA player of all time."
print(player1, player2, player3)

#Global Variables
player1 = "Greatest Rebounder of Alltime."

def myfunc():
  global player1
  player1 = "The Greatest Shooter of Alltime."

myfunc()

print("Stephen Curry is " + player1)

#