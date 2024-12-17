num1=float(input("enter your first number: "))
num2=float(input("enter your second number: "))
num3=float(input("enter your third number: "))
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)


score = float(input("Choose a score (0-100): "))
if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
elif score < 60 and score >= 0:
    print("F")
else:
    print("Invalid score")


num=float(input("enter your number: "))
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative.")
else:
    print("The number is zero.")


num_1=int(input("enter your first number: "))
num_2=int(input("enter your second number: "))
sum = 0
for num in range(num_1, num_2 + 1):
    sum += num

# Print the sum
print("The sum is:", sum)


number = int(input("Enter a number: "))

if number < 2:
    print(number, "is not a prime number.")
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(number, "is not a prime number.")
    else:
        print(number, "is a prime number.")


list = [15, 30, 45, 60, 75]

print("First element:", list[0]) 
print("Third element:", list[2])  
print("Last element:", list[4])


list = [5, "apple", 3.14, True, None, 42, "GOA", 9, 7.6, False, "hello", 100, 45.67, "world", 88, 15, "Python", 200, "java", -5]

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print(list[7])
print(list[8])
print(list[9])
print(list[10])
print(list[11])
print(list[12])
print(list[13])
print(list[14])
print(list[15])
print(list[16])
print(list[17])
print(list[18])
print(list[19])




