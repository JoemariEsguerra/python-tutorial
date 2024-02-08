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