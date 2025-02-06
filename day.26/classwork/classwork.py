def greet(name):
    print(f"გამარჯობა, {name}")

greet("ნანუკა")

def manual_range(start, end, step):
    for num in range(start, end, step):
        if num % 2 == 0:
            print(num)

manual_range(1, 10, 1)
manual_range(0, 20, 2)
manual_range(5, 30, 3)
manual_range(0, 15, 4)
manual_range(10, 50, 5)


def manual_len(my_list):
    count = 0
    for item in my_list:
        count += 1
    print(f"სიის სიგრძე არის: {count}")


manual_len([1, 2, 3, 4])
manual_len([10, 20, 30])
manual_len([5, 10, 15, 20, 25, 30])
manual_len(["apple", "banana", "cherry"])
manual_len([True, False, True, False])