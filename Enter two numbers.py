'''Takes 2 numbers as parameters and returns the product'''

keep_asking = True
while keep_asking == True:
    try:
        num1 = float(input("What is your first number?"))
        num2 = float(input("What is your second number?"))
        keep_asking = False

    except ValueError:
        print("please enter a number")

