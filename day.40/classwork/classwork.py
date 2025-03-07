def greet():
    return "hello world!"

def count_sheeps(sheep):
    return sheep.count(True)

def no_space(x):
    return x.replace(" ", "")

def double_integer(i):
    return i*2

def greet(name):
    return str(f"Hello, {name} how are you doing today?")

def boolean_to_string(b):
    return str(b)

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    


def litres(time):
    return time//2

def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year //100 + 1
    

    def digitize(n):
        starting_str = str(n)
    reversed_str = starting_str[::-1]
    
    res_list=[]
    for i in reversed_str:
        res_list.append(int(i))
        
    return res_list


def maps(a):
    saver = []
    for i in a:
        saver.append(i*2)
    return saver


def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    elif flower1 %2 ==1 and flower2 % 2 == 0:
        return True
    else:
        return False

def sum_array(a):
    return sum(a)