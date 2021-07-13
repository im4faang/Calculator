import os
from art import logo


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calculator():
  should_end = False
  print(logo)
  num1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)

  while not should_end:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    if choice == "y":
      num1 = answer
    elif choice == "n":
      should_end = True
      os.system("clear")
      calculator()

calculator()
