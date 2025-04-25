numbers = [1, 2, 3, 4, 5, 6, 12, 15, 18, 21, 33, 44, 55, 66, 78, 99, 100]
strings = ["apple", "", "banana", "kiwi", "", "pineapple", "grape", "orange", "", "watermelon"]
names = ["Anamaria", "Biba", "Angela", "Mariami", "Amanda", "Tomi", "Anna", "Steve"]
words = ["tree", "sky", "river", "cloud", "earth", "wind", "fire", "light"]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

greater_than_10 = list(filter(lambda x: x > 10, numbers))

long_strings = list(filter(lambda x: len(x) > 5, strings))

non_empty_strings = list(filter(lambda x: x != "", strings))

positive_numbers = list(filter(lambda x: x > 0, numbers))

names_start_with_A = list(filter(lambda x: x.startswith('A'), names))

divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

words_with_e = list(filter(lambda x: 'e' in x, words))

no_none_values = list(filter(lambda x: x is not None, [1, None, 2, None, 3, 4, None]))

less_than_or_equal_50 = list(filter(lambda x: x <= 50, numbers))

print("Even numbers:", even_numbers)
print("Greater than 10:", greater_than_10)
print("Strings longer than 5:", long_strings)
print("Non-empty strings:", non_empty_strings)
print("Positive numbers:", positive_numbers)
print("Names starting with A:", names_start_with_A)
print("Divisible by 3:", divisible_by_3)
print("Words with 'e':", words_with_e)
print("Without None values:", no_none_values)
print("Less than or equal to 50:", less_than_or_equal_50)

is_even = lambda x: x % 2 == 0
print("Is 7 even?", is_even(7))