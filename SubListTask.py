details = []
keep_asking = True
while keep_asking == True:
    try:
        name = input("Enter your name: ")
        if name.lower() == "stop":
            keep_asking = False
        else:
            age = int(input("Enter your age: "))
            if name.strip(" ") ==  "":
                print("invalid name")
            elif age < 0:
                print("invalid age")
            elif age > 150:
                print("zoinks you are old please be younger and enter everything again")
            elif age == "":
                print("invalid age")
            else:
                details.append([name, age])
    except ValueError:
        print("please enter a valid number mah drilla")
for i in range(len(details)):
  print(f"{i+1}. {details[i][0]} {details[i][1]}")

