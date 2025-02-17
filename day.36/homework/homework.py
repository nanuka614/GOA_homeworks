
def string_to_number(s):
    return int(s)

def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest


def summation(num):
    return num * (num + 1) // 2


def make_upper_case(s):
    return s.upper()


def remove_spaces(x):
    return x.replace(" ", "")

def greet(name):
    return f"Hello, {name} how are you doing today?"

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
    


def century(year):
    return (year + 99) // 100


def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else:
        return False