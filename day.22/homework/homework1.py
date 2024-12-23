list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for x in list1:
    print(x)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    print(list[num1:num2])  
elif num2 > num1:
    print(list[num2:num1])  
else:
    print([])


list2 = [10, 20, 30, 40, 50]

print("First element:", list[0])   
print("Third element:", list[2])  
print("Last element:", list[-1])



strings = ["apple", "banana", "cherry", "grapes", "orange"]

print("Reversed list:", strings[::-1])


words = ["red", "blue", "purple", "pink", "green", "black", "gray"]

print("Every second word:", words[::2])


numbers = [60, 70, 80, 90, 100]

numbers[3] = 100

print("Modified list:", numbers)