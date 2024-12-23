list = 10, "hello", 3.14, True, "Python", 42, "world", 7.5, False, "end"

num = int(input("Enter your number: "))

if 0 <= num and num < 10:
    i = 0
    for x in list:
        if i == num:
            print("ელემენტი არის: " + str(x))
        i = i + 1

elif -10 <= num and num <= -1:
    i = -10
    for x in list:
        if i == num:
            print("ელემენტი არის: " + str(x))
        i = i + 1

else:
    print("რიცხვი არასწორია!")



list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for x in list1:
    print(x*2)
    print(x/2)