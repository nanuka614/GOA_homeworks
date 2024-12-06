for i in range(5):
    num = int(input("Enter a number: "))

    # Check if the number is even or odd
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")



correct_password = "Goa best"
counter = 0
user_password = input("Enter the password: ")

# Keep asking until the user enters the correct password
while user_password != correct_password:
    user_password = input("Enter the password: ")
    
    if user_password == correct_password:
        print("Password correct!")
    else:
        counter += 1
        print("Incorrect password. Try again.")

# Print the number of incorrect attempts
print("Incorrect password attempts:", counter)



num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Take the operator as input
operator = input("Enter the operator (+, -, *, /): ")

result = None

if operator == "+":
    result = num1 + num2

if operator == "-":
    result = num1 - num2

if operator == "*":
    result = num1 * num2

if operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

if result is None:
    result = "Invalid operator."

# Display the result
print("Result:", result)


