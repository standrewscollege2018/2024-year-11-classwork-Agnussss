'''Tests wether blood donators are eligible'''



keep_asking = True
while keep_asking == True:
    #Trys to catch any invalid inputs
    try :
        #asks for age and weight
        age = int(input("Please enter your age: "))
        weight = float(input("Please enter your weight: "))
        #stops the while loop
        keep_asking = False
    #if invalid input is entered will print
    except ValueError:
        print("please enter your Age and weight with only numbers")

if age >= 16 and weight >= 50 :
    #if eligible will print
    print("You are eligible!")

else:
    #if not eligible will print
    print("You aren't eligible")
