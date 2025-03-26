try:
    input = input("Please enter a number: ")
    number = float(input)  
    print(f"You enter the number: {number}")

except ValueError:
    print("Error: Please enter a valid number.")




my_list = [1, 2, 3, 4, 5]  
try:
    print(my_list[6])

except IndexError:
    print("Error: The index you tried to access does not exist in the list.")



try:
    result = "num" + 5

except TypeError:
    print("Error: You can't add a number to a string. Please convert the number to a string first.")