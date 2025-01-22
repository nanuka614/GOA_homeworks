paragraph = "The cat sat on the mat, and the dog watched from the window."

count_the = paragraph.count("the")

print(f"The word 'the' appears {count_the} times.")




string = "hello world, welcome to Python."

char = input("Enter a character to count its occurrences: ")

count_char = string.count(char)

print(f"The character '{char}' appears {count_char} times.")




def count_word_occurrences(text, word):
    return text.count(word)

text = "The cat and the dog and the mouse."
word = "the"
count = count_word_occurrences(text, word)

print(f"The word '{word}' appears {count} times.")




string = "hello world, hello Python!"

index_hello = string.find("hello")

print(f"The word 'hello' first appears at index {index_hello}.")




def find_char_index(string, char):
    return string.find(char)

string = "hello world"
char = input("Enter a character to find its index: ")
index_char = find_char_index(string, char)

if index_char != -1:
    print(f"The character '{char}' is at index {index_char}.")
else:
    print(f"The character '{char}' was not found.")




string = "hello world"

is_lowercase = string.islower()

print(f"Are all characters in the string lowercase? {is_lowercase}")




def is_all_lowercase(input_string):
    return input_string.islower()

input_string = "hello"
result = is_all_lowercase(input_string)

print(f"Is the string completely in lowercase? {result}")




user_input = input("Enter a string: ")

if user_input.islower():
    print("The string contains only lowercase letters.")
else:
    print("The string contains characters that are not lowercase.")




user_input = input("Enter a string: ")

is_uppercase = user_input.isupper()

print(f"Are all characters in the string uppercase? {is_uppercase}")




def is_all_uppercase(input_string):
    return input_string.isupper()

input_string = "HELLO"
result = is_all_uppercase(input_string)

print(f"Is the string completely in uppercase? {result}")




user_input = input("Enter a string: ")

if user_input.isupper():
    print("The string is in uppercase.")
else:
    print("The string is not in uppercase.")





sentence = "The dog is playing with the dog."

updated_sentence = sentence.replace("dog", "cat")

print(updated_sentence)




def replace_spaces_with_underscores(input_string):
    return input_string.replace(" ", "_")

input_string = "Hello world, welcome to Python."
result = replace_spaces_with_underscores(input_string)

print(result)




tring = "Hello, World!"

swapped_string = string.swapcase()

print(swapped_string)




def swap_case_in_sentence(sentence):
    return sentence.swapcase()

sentence = "Hello World! Python is Fun."
result = swap_case_in_sentence(sentence)

print(result)



