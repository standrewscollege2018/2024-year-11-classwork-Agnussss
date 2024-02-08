'''this might do something'''

keep_asking = True
while keep_asking == True:
    try:
        x = float(input("Enter a positive number: "))
        if x>= 0:
            keep_asking = False
        else:
            print("Please enter a positive number")

    except ValueError:
        print("number please")

print(f"{x} doubled is {x*2}")
