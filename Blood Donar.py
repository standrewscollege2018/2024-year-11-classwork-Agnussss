'''Tests wether blood donators are eligible'''


keep_asking = True
while keep_asking == True:
    #Trys to catch any invalid inputs
    try :
        #asks for age and weight
        age = int(input("enter your age: "))
        weight = int(input("enter your weight: "))
        #stops the while loop
        keep_asking = False
    #if invalid input is entered will print
    except ValueError:
        print("please enter your Age and weight with only numbers")

def check(user ,req, user2, req2):
    if user >= req:
        if user2 >= req2:
            print("you are eligible")

        else:
            print("Sufficient age but insufficient weight")
    else:
        if user2 >= req2:
            print("Insufficient age but correct weight")

        else:
            print("Insufficient age and weight")


check(age, 16, weight, 50)


