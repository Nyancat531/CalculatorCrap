# Calculator Program
# v2.5.12 By Jake Marchewitz

import math

# Keeps program running after 1 calculation
going = True

# Re-usable calculations with x(1st number) and y(2nd number) input slots

print ("Welcome to the Calculator v2.5.12")
print ("Created By Jake Marchewitz\n")
print ("\n")

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def exponent(x, y):
   return x ** y

def root(x, y):
   return (x**(1/y)) 

while going:

   # User operation input selections
   print("Select your operation.")
   print("Add")
   print("Subtract")
   print("Multiply")
   print("Divide")
   print("Exponent")
   print("Root")
   print("Quit\n")

   # Raw user input
   choice = raw_input("Enter choice(Add/Subtract/Multiply/Divide/Exponent/Root/Quit): ")

   # Responds based on raw input and inputs into corresponding calculations
   if choice.lower() == 'add':
      num1 = float(raw_input("Enter first number: "))
      num2 = float(raw_input("Enter second number: "))
      print add(num1,num2)
      print ("\n")

   elif choice.lower() == 'subtract':
      num1 = float(raw_input("Enter first number: "))
      num2 = float(raw_input("Enter second number: "))
      print subtract(num1,num2)
      print ("\n")

   elif choice.lower() == 'multiply':
      num1 = float(raw_input("Enter first number: "))
      num2 = float(raw_input("Enter second number: "))
      print multiply(num1,num2)
      print ("\n")

   elif choice.lower() == 'divide':
      num1 = float(raw_input("Enter first number: "))
      num2 = float(raw_input("Enter second number: "))
      print divide(num1,num2)
      print ("\n")

   elif choice.lower() == 'exponent':
      num1 = float(raw_input("Enter base number: "))
      num2 = float(raw_input("Enter exponential power: "))
      print exponent(num1,num2)
      print ("\n")

   elif choice.lower() == 'root':
      num1 = float(raw_input("Enter radicand: "))
      num2 = float(raw_input("Enter index: "))
      print root(num1,num2)
      print ("\n")
      
   #Terminates program
   elif choice.lower() == 'quit':
      quit()

   else:
      print("Invalid input")
