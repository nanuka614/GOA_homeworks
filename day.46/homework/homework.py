list1 = [i for i in range(1, 11)]
print(list1)

list2 = [x**3 for x in range(1, 6)]
print(list2)

list3 = [y for y in range(1, 21) if y % 2 == 0]
print(list3)

words = ["nanu", "jumber", "stiles", "frankie"]
list4 = [i[0] for i in words]
print(list4)

list5 = [x.upper() for x in words]
print(list5)

list6 = [y for y in range(1, 51) if y % 3 == 0]
print(list6)

list7 = [z for z in words if len(z) > 4]
print(list7)

celsius = [0, 30, 50, 100]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print(fahrenheit)

fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(18)]
print(fibonacci)
