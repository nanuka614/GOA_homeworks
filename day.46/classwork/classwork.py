#``საკლასო დავალება:

#შექმენით ფუნქცია სახელად manual_list, რომელსაც ექნება 4 პარამეტრი: start, end, step, user_num.

#თქვენი დავალებაა, რომ ფუნქციამ დააბრუნოს სია, რომელშიც იქნება რიცხვები არჩეული (start, end, step) 
# დიაპაზონის მიხედვით, უბრალოდ ეს რიცხვები მეტი უნდა იყოს user_num.

#ფუნქცია გამოიძახეთ 3-ჯერ, განსხვავებული არგუმენტებით```

def manual_list(start, end, step, user_num):
    return [x + user_num for x in range(start, end, step)]


print(manual_list(1, 5, 1, 2))  
print(manual_list(0, 6, 2, 1))  
print(manual_list(2, 8, 2, 3))


#Create a list comprehension that generates a list of all numbers between 1 and 100 that are divisible by either 3 or 5, but not both.

list = [i for i in range(1, 101) if (i % 5 == 0 or i % 3 == 0) and i % 15 != 0]
print(list)

#Create a list comprehension that generates a list of all palindromic numbers between 10 and 200 
# (a palindromic number reads the same forward and backward).str and slicing

list1 = [y for y in range(10, 201) if str(y) == str(y)[::-1]]
print(list1)


