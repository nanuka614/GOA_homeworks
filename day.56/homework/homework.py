print("nanuka")

print('"lorem."')

print("Roses are red")
print("Violets are blue")
print("Code is sweet and so are you")

print(2 + 3)

print("*")
print("**")
print("***")
print("****")

num_str = "42"
num_int = int(num_str)
print(num_int)

a = 3.5
b = 2.5
print(a + b)

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

x = 10
y = "text"
z = 3.14
print(type(x))
print(type(y))
print(type(z))


age = int(input("How old are you? "))
print("Next year you will be", age + 1)

name = input("What is your name? ")
print("Hello, " + name + "!")

age = int(input("What is your age? "))
print("Next year you will be", age + 1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is", num1 + num2)

color = input("What is your favorite color? ")
print("Your favorite color is " + color + "!")

height = int(input("Enter your height in cm: "))
if height > 150:
    print("You are tall enough.")
else:
    print("You are not tall enough.")

for i in range(1, 6):
    print(i)

word = "Python"
for letter in word:
    print(letter)

total = 0
for i in range(1, 11):
    total += i
print(total)