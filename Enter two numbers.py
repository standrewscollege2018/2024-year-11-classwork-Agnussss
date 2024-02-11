'''Takes 2 numbers as parameters and returns the product'''

def multiply(number1, number2):
    return number1 * number2

keep_asking = True
while keep_asking == True:
    try:
        num1 = float(input("What is your first number?"))
        num2 = float(input("What is your second number?"))
        keep_asking = False

    except ValueError:
        print("please enter a number")

print(multiply(num1, num2))
