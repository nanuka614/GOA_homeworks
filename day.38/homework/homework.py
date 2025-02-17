tuple = (10, 20, 30, 40, 50)

second_element = tuple[1]

last_element = tuple[-1]

middle_slice = tuple[1:4]

print("Second element:", second_element)
print("Last element:", last_element)
print("Middle slice:", middle_slice)




my_tuple = (10, 20, 30, 40, 50)

a, b, c, d, e = my_tuple

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)




my_list = [10, 20, 30, 20, 40, 50, 10, 30]

my_set = set(my_list)

unique_list = list(my_set)

print("List with duplicates removed:", unique_list)




my_tuple1 = (10, 20, 20, 30, 40, 20, 50)

count_20 = my_tuple1.count(20)

index_20 = my_tuple1.index(20)

print("Occurrences of 20:", count_20)
print("Index of first occurrence of 20:", index_20)





my_set = {10, 20, 30, 40, 50}

my_set.add(60)

my_set.remove(20)

is_present = 30 in my_set

print("Updated set:", my_set)
print("Is 30 present in the set?", is_present)





set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

union_set = set1.union(set2)

intersection_set = set1.intersection(set2)

difference_set = set1.difference(set2)

print("Union of sets:", union_set)
print("Intersection of sets:", intersection_set)
print("Difference of sets:", difference_set)




my_tuple = (10, 20, 30, 40, 50)

my_tuple[1] = 100  # This will raise an error