
colors = ("red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white")

print(colors[0])  
print(colors[1])  
print(colors[2])  
print(colors[3])  
print(colors[4])  
print(colors[5])  
print(colors[6])  
print(colors[7])  
print(colors[8])  
print(colors[9])



colors = ("red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white")
for color in colors:
    print(color)




def no_duplicates(user_list):
    return list(set(user_list))


print(no_duplicates([1, 2, 3, 4, 5, 5, 3]))
print(no_duplicates([ 'banana', 'apple', 'orange', 'banana', 'apple']))
print(no_duplicates([10, 20, 30, 40, 10, 50, 20]))