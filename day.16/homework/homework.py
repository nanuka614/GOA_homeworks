for i in range(50):  # 0-დან 49-მდე ციკლის გამეორება 
    print("GOA BEST!!!")


count = 0   
while count < 50:  # ციკლი გაგრძელდება, სანამ count 50-ზე ნაკლებია
    print("GOA BEST!!!")
    count += 1 


count = 1
while count <= 10:
    print(count)  # Print the current number
    count += 1 


num = 2
while num <= 20:
    print(num) 
    num += 2    # Increment by 2 to get the next even number


correct_password = "123"
user_password = input("Enter the password: ")
# Keep asking until the user enters the correct password
while user_password != correct_password:
    user_password = input("Enter the password: ")# Prompt the user to enter the password

print("Access granted!")


count = 10
while count > 0:
    print(count)
    count -= 1    # Decrement the counter by 1

print("Blast off!")


correct_username = "nanu"
correct_password = "12345"

username = input("Enter your username: ")
password = input("Enter your password: ")

while username != correct_username or password != correct_password:
    print("Incorrect username or password. try again.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

print("Access granted!")


num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
x=num
while i > 0:
    factorial *= i  # Multiply the current value of factorial by i
    i -= 1           # Decrease i by 1

print("The factorial is:", factorial)

