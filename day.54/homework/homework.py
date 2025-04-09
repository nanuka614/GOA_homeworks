def greet(func):
    func()
def say_hello():
    print("Hello! Welcome!")



def multiply_by(factor):
    def multiplier(number):
        return number * factor
    return multiplier

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    result = num1 / num2
    print("The result of division is:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")



my_list = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter an index to access list: "))
    if index < 0 or index >= len(my_list):
        raise IndexError("Error: Index out of range.")
    print("The value at index", index, "is:", my_list[index])

except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid number.")



user_input = input("Enter a number: ")
try:
    num = int(user_input)
    print("The integer value is:", num)

except ValueError:
    print("Error: Please enter a valid integer.")



my_dict = {'name': 'Ana', 'age': 15}
key = input("Enter a key to access from the dictionary: ")

try:
    print("The value for", key, "is:", my_dict[key])

except ValueError:
    print("Error: Invalid input.")