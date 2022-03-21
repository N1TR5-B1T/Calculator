number1 = input("First Number: ")
operation = input("Choose an operation, (+, -, /, *): ")
number2 = input("Second Number: ")

if operation == ("+"):
  print("Answer:", float(number1) + float(number2))

if operation == ("-"):
  print("Answer:", float(number1) - float(number2))

if operation == ("/"):
  print("Answer:", float(number1) / float(number2))

if operation == ("*"):
  print("Answer:", float(number1) * float(number2))