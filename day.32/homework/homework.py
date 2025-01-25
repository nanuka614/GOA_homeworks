def welcome_message(name, age):
    return f"Hello {name}! You are {age} years old. Welcome!"

print(welcome_message("nanuka", 14))



def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"

print(format_name("nanu", "dekanosidze"))



def reverse_string(sentence):
    reversed_sentence = sentence[::-1]
    return f"The reversed string is: {reversed_sentence}"

print(reverse_string("hello"))



def sentence_to_words(sentence):
    return sentence.split()

print(sentence_to_words("This is a sentence"))



def csv_to_list(csv_string):
    return csv_string.split(',')

print(csv_to_list("red,purple,orange"))



def split_paragraph(paragraph):
    return paragraph.split('.')

print(split_paragraph("this is a example!"))



def append_item(my_list, item):
    my_list.append(item)
    return my_list

my_list = [1, 2, 3]
print(append_item(my_list, 4))



def append_items(my_list, items):
    my_list.extend(items)
    return my_list

my_list = [1, 2]
items_to_add = [3, 4, 5]
print(append_items(my_list, items_to_add))



def append_all_elements(list1, list2):
    list1.extend(list2)
    return list1

list1 = [1, 2]
list2 = [3, 4]
print(append_all_elements(list1, list2))



def insert_item(my_list, index, item):
    my_list.insert(index, item)
    return my_list

my_list = [1, 2, 4]
print(insert_item(my_list, 2, 3))



def insert_at_beginning(my_list, item):
    my_list.insert(0, item)
    return my_list

my_list = [2, 3, 4]
print(insert_at_beginning(my_list, 1))



def insert_at_end(my_list, item):
    my_list.insert(len(my_list), item)
    return my_list

my_list = [1, 2, 3]
print(insert_at_end(my_list, 4))