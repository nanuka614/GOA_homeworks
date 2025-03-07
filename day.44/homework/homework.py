def bmi(weight, height):
    # Step 1: Calculate the BMI value using the formula: BMI = weight / height^2
    bmi_value = weight / height**2  # This is the formula for BMI, where weight is in kg and height is in meters.
    
    # Step 2: Check if the BMI falls under the "Underweight" category
    if bmi_value <= 18.5: 
        return "Underweight"  # If the BMI is less than or equal to 18.5, return "Underweight"
    
    # Step 3: Check if the BMI falls under the "Normal" category
    elif bmi_value <= 25.0: 
        return "Normal"  # If the BMI is between 18.6 and 25.0, return "Normal"
    
    # Step 4: Check if the BMI falls under the "Overweight" category
    elif bmi_value <= 30.0: 
        return "Overweight"  # If the BMI is between 25.1 and 30.0, return "Overweight"
    
    # Step 5: If the BMI is greater than 30, return "Obese"
    return "Obese"  # If the BMI is greater than 30, return "Obese"



def reverse_array(n):
    result = []
    for i in range(n, 0, -1):
        result.append(i)
    return result


def rps(p1, p2):

    if p1 == p2:
        return "Draw!"
    
    if (p1 == "rock" and p2 == "scissors") or \
        (p1 == "scissors" and p2 == "paper") or \
        (p1 == "paper" and p2 == "rock"):
        return "Player 1 won!"
    return "Player 2 won!"



def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    return False



def count_sheep(n):
    return ''.join([f"{i} sheep..." for i in range(1, n + 1)])



def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

