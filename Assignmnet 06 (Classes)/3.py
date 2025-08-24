class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b


# Example usage
calc = Calculator()

print("Select operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {calc.add(num1, num2)}")
elif choice == '2':
    print(f"Result: {calc.subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {calc.multiply(num1, num2)}")
elif choice == '4':
    print(f"Result: {calc.divide(num1, num2)}")
else:
    print("Invalid input")
