name = input("name: ")
choice = input("'u' or 'l': ")



if choice == "u":
    print(name.upper())
elif choice == "l":
    print(name.lower())
else:
    print("wrong information")


main_str = input("Enter the main string: ")
str_to_count = input("Enter the string to count: ")

print(main_str.count(str_to_count))



def manual_swapcase(text):
    return text.swapcase()

input_text = "Hello World!"
swapped_text = manual_swapcase(input_text)
print(swapped_text)




