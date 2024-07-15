num1 = float(input("Enter your first number"))
num2 = float(input("Enter your second number"))

print("Enter an Operator")
print(" Press + for additon\n Press - for subtraction\n Press / for division\n Press * for Multiplication")
op = input("Operator").strip()

result = None

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '/':
    result = num1 / num2
elif op == '*':
    result = num1 * num2
else:
    print("invalid operator entered")

if result is not None:
    print("Result:", result)


