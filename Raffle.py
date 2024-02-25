import random
print("Welcome to the Raffle Draw!")
prize = input("What is the prize? ")
asking_value = True
while asking_value == True:
    try:
        value = int(input("How much is the prize worth? "))
        asking_value = False
    except ValueError:
        print("please enter a number")

print("Enter the names of the people who entered the raffle. Enter 'end' to start the draw.")
names = []
keep_asking = True
while keep_asking == True:
  name = input("Enter a name: ")
  if name == "end":
    keep_asking = False
  else:
    names.append(name)
print("There are", len(names), "people in the draw.")
print("The prize is", prize, "and it is worth", value, "dollars.")
winner = random.choice(names)
print("The winner is", winner, "who won", prize, "for", value, "dollars")
