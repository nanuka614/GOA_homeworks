def manual_index(main_string, search_string):
    for i in range(len(main_string)):
        if main_string[i:i+len(search_string)] == search_string:
            return i
    return -1  


print(manual_index("Hello, world!", "world"))  
print(manual_index("Python programming", "gram"))  
print(manual_index("Testing manual index", "manual"))  
print(manual_index("OpenAI Assistant", "AI"))  
print(manual_index("abcdef", "z"))