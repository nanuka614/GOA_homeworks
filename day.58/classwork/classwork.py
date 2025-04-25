variable = lambda str: str[::-1].capitalize()

print(variable("red"))     
print(variable("blue"))    
print(variable("green"))


num = lambda x: x*2
print(num(3))


print(list(map(lambda x: x ** 2, [1,2,3,4,5,6,7,8,9,10])))