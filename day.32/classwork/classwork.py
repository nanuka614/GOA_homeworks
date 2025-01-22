name = input("enter your name: ")
surname = input("enter your surname: ")
age = int(input("enter your age: "))

def generate_big_sentence(name, surname, age):
    print("my name is {}, my surname is {}, and i am {}, years old.".format(name, surname, age))

generate_big_sentence(name, surname, age)




def generate_big_sentence(name, surname, age):
    print(f"my name is {name}, my surname is {surname}, and i am {age} years old.")

name = input("enter your name: ")
surname = input("enter your surname: ")
age = int(input("enter your age: "))

generate_big_sentence(name, surname, age)




main_string = input("enter the main string: ")
string_to_split = ("enter the string to split: ")

def my_split(main_string, string_to_split):
    result = main_string.split(string_to_split)
    print(result)

my_split(main_string, string_to_split)



def manual_append(main_list, item_to_insert):
    main_list.insert(len(main_list), item_to_insert)

my_list = [3, 7, 5]
manual_append(my_list, 4)
print(my_list)



