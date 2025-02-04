def hello_world():
    print("Hello, World!")


def sum_of_two_numbers(x, y):
    print(x + y)


def multiply_by_ten(a):
    return a * 10



def greet(name="Guest"):
    print(f"Hello, {name}!")



def outer_function():
    def inner_function():
        print("This is the inner function!")
    
    inner_function()



def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")



def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num



def positive_numbers(numbers):
    positive_list = []
    for num in numbers:
        if num > 0:
            positive_list.append(num)
    return positive_list




def sum_divisible_by_three():
    total_sum = 0
    for i in range(1, 101):
        if i % 3 == 0:
            total_sum += i
    return total_sum