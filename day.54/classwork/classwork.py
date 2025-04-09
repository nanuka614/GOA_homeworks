try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    if num2 == 0:
        raise ValueError("cannott divide by zero!")


    res = num1 / num2
    print("the result is:" , res)

except:
    print("something went wrong.")
finally:
    print("Operation complete.")



def square(x):
    return x * x

def apply_to_list(func, values):
    return [func(x) for x in values]