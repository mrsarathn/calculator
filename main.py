from art import logo
from replit import clear
# Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return (n1 - n2)

#Multiply
def multiply(n1, n2):
  return (n1*n2)

# Divide
def divide(n1, n2):
  if (n2 != 0):
    return (n1/n2)
  else:
    return "Divisor is 0"


#Dictionary
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  num1 = float(input("Enter first number: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operator = input("Which symbol do you choose?")
    num2     = int(input("Enter next number: "))
    answer = operations[operator](num1, num2)
    print(f"{num1} {operator} {num2} = {answer}")
    if(input(f"Enter 'y' to continue the calculation with {answer}, or 'n' to start afresh")) == 'n':
      should_continue = False
      clear()
      calculator()
    else:
      num1 = answer

     


calculator()

  




