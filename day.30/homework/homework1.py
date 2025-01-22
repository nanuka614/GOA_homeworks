sentence = "sample sentence."
uppercase_sentence = sentence.upper()
print(uppercase_sentence)



user_name = input("Enter your name: ")

uppercase_name = user_name.upper()
print(f"Your name in uppercase is: {uppercase_name}")



lowercase_strings = ["hello", "world", "python", "programming"]

for i in range(len(lowercase_strings)):
    lowercase_strings[i] = lowercase_strings[i].upper()

print(lowercase_strings)



sentence = "This Is A Mixed CASE Sentence."

lowercase_sentence = sentence.lower()
print(lowercase_sentence)




email = input("Enter your email address: ")

email_lowercase = email.lower()

print(f"Your email in lowercase is: {email_lowercase}")




def convert_to_lowercase(input_string):
    return input_string.lower()

mixed_case_string = "ThIs Is A MiXeD CaSe StRiNg"
lowercase_string = convert_to_lowercase(mixed_case_string)

print(lowercase_string)




sentence = input("Enter a sentence: ")

capitalized_sentence = sentence.capitalize()

print(f"Capitalized sentence: {capitalized_sentence}")




def capitalize_first_letter(input_string):
    return input_string.capitalize()

input_string = "hello, world!"
capitalized_string = capitalize_first_letter(input_string)

print(capitalized_string)




lowercase_strings = ["hello", "world", "python", "programming"]

for i in range(len(lowercase_strings)):
    lowercase_strings[i] = lowercase_strings[i].capitalize()

print(lowercase_strings)



sentence = "I am learning Python"

position = sentence.find("Python")

print(f"The first occurrence of 'Python' is at index: {position}")




main_string = input("Enter a string: ")
substring = input("Enter the substring to search for: ")

index = main_string.find(substring)

if index != -1:
    print(f"The substring '{substring}' starts at index: {index}")
else:
    print(f"The substring '{substring}' was not found.")



def find_char_index(input_string, char):
    return input_string.find(char)

input_string = "Hello, world!"
char = "o"
index = find_char_index(input_string, char)

if index != -1:
    print(f"The character '{char}' is at index: {index}")
else:
    print(f"The character '{char}' was not found.")




user_string = input("Enter a string: ")

string_length = len(user_string)

print(f"The length of your string is: {string_length}")




def get_lengths_of_strings(string_list):
    return [len(string) for string in string_list]

strings = ["apple", "banana", "cherry"]
lengths = get_lengths_of_strings(strings)

print(lengths)
