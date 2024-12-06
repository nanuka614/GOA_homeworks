num=0
while num <= 20:
    print(num)  
    num += 2 

for num in range(1, 21, 2):
    print(num)


for num in range(10, 31):
    if num % 2 == 0:  
        print(num, "- even")
    else: 
        print(num, "- odd")


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if num1 > num2:
    even_numbers = (num for num in range(num2, num1 + 1) if num % 2 == 0)
    print("Even numbers:", even_numbers)
    print("Sum:", sum(even_numbers))
else:
    odd_numbers = (num for num in range(num1, num2 + 1) if num % 2 != 0)
    print("Odd numbers:", odd_numbers)
    print("Sum:", sum(odd_numbers))