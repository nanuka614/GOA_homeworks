#რიცხვის შეყვანა
age = int(input("გთხოვთ, შეიყვანეთ თქვენი ასაკი: "))

# ათ წელიწადში 
future_age = age + 10

# შედეგი
print("ათ წელში თქვენ იქნებით", future_age, "წლის.")

#რიცხვების შეყვანა
age1 = int(input("გთხოვთ, შეიყვანეთ პირველი ადამიანის ასაკი: "))
age2 = int(input("გთხოვთ, შეიყვანეთ მეორე ადამიანის ასაკი: "))
age3 = int(input("გთხოვთ, შეიყვანეთ მესამე ადამიანის ასაკი: "))

# ასაკების ჯამი
total_age = age1 + age2 + age3

# საშუალო არითმეტიკული
average_age = total_age / 3

# შედეგის დაბეჭდვა
print("სამი ადამიანის ასაკების საშუალო არითმეტიკული არის:", average_age)


#რიცხვების შეყვანა
num1 = int(input("გთხოვთ, შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("გთხოვთ, შეიყვანეთ მეორე რიცხვი: "))

# გამოთვლები
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
power1 = num1 ** num2
power2 = num2 ** num1

# შედეგი
print("ჯამი:", sum_result)
print("სხვაობა:", difference)
print("ნამრავლი:", product)
print("განაყოფი:", quotient)
print("პირველი რიცხვი ხარისხად მეორეზე:", power1)
print("მეორე რიცხვი ხარისხად პირველზე:", power2)

#რიცხვები
a = 100
b = 10
c = 1000

# ჯამის გამოთვლა
sum_result = a + b + c

# სხვაობის გამოთვლა
difference_result = a - b - c

# ნამრავლის გამოთვლა
product_result = a * b * c

# განაყოფის გამოთვლა 
division_result = a / b / c

# შედეგები
print("ჯამი:", sum_result)
print("სხვაობა:", difference_result)
print("ნამრავლი:", product_result)
print("განაყოფი:", division_result)