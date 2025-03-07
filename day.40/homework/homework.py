def past(h, m, s):
    sum_of_seconds = 0
    sum_of_seconds += h * 3600
    sum_of_seconds += m * 60
    sum_of_seconds += s
    result = sum_of_seconds * 1000
    return result



def abbrev_name(name):
    new_list = name.split(" ")
    return f"{new_list[0][0].upper()}.{new_list[1][0].upper()}"



def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"



    def make_upper_case(s):
        return s.upper()
    



    def paperwork(n, m):
        if n < 0 or m < 0:
            return 0
    return n * m



# This function returns the string "hello world!"
def greet():
    return "hello world!"



# This function counts how many True values are in the list 'sheep'.
def count_sheeps(sheep):
    return sheep.count(True)



# This function removes all spaces from the input string 'x'.
def no_space(x):
    return x.replace(" ", "")



# This function doubles the integer 'i' and returns the result.
def double_integer(i):
    return i*2



# This function returns a greeting string with the provided 'name'.
def greet(name):
    return str(f"Hello, {name} how are you doing today?")



# This function converts the boolean 'b' into a string ('True' or 'False').
def boolean_to_string(b):
    return str(b)



# This function performs basic arithmetic operations based on the operator ('+', '-', '*', '/').
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2



# This function calculates how many liters of water are needed based on the input time (half a liter per hour).
def litres(time):
    return time//2



# This function calculates the century of a given 'year'. If the year is divisible by 100, it returns the quotient; otherwise, it adds 1 to the quotient.
def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year //100 + 1



# This function takes a number 'n', converts it to a string, reverses it, and returns the digits in reverse order as a list of integers.
def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]
    
    res_list=[]
    for i in reversed_str:
        res_list.append(int(i))
        
    return res_list



# This function takes a list 'a', doubles each element in it, and returns a new list with the results.
def maps(a):
    saver = []
    for i in a:
        saver.append(i*2)
    return saver



# This function checks if one flower is odd and the other is even. It returns True if that condition is met.
def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    elif flower1 %2 ==1 and flower2 % 2 == 0:
        return True
    else:
        return False



# This function returns the sum of all the numbers in the array 'a'.
def sum_array(a):
    return sum(a)