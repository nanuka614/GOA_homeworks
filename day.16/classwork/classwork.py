number = int(input("Enter a number: "))
sum_of_range = 0
for i in range(number + 1):
    sum_of_range += i
print(f"The sum of numbers from 0 to {number} is: {sum_of_range}")


correct_password = "your_password"
attempts = 0
while True:
    user_password = input("Enter the password: ")
    attempts += 1
    if user_password == correct_password:
        print("access granted")
        print(f"Password attempts: {attempts}")
        break
    else:
        print("Incorrect password, try again.")


my_num = 7
attempts = 0
while True:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1
    if guess == my_num:
        print(f"you guessed it! You guessed in {attempts} attempts.")
        break
    else:
        print("Wrong number, try again.")
