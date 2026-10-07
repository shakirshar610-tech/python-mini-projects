def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    raise ValueError("Unknown operator.")

a = float(input("First number: "))
op = input("Operator (+ - * /): ").strip()
b = float(input("Second number: "))

try:
    print("Result:", calculate(a, op, b))
except ValueError as error:
    print(error)
