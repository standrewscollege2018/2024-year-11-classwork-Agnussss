''' I am a docstring '''

# Vehicles contains sub-lists for each vehicle, containing name number of seats and stock
vehicles = [["Suzuki Van", 2, 1], ["Toyota Corolla", 4, 1], ["Honda CRV", 4, 1 ], ["Suzuki Swift", 4, 1], ["Mitsubishi Airtrek", 4, 1], ["Nissan DC Ute", 4, 1], ["Toyota Previa", 7, 1], ["Toyota Hi Ace", 12, 2]]
# Bookings will contain sub lists with thr vehicle and name of person booking it
bookings = []
count = 0
# Functions
''' Docstring describes functions'''
def display_vehicles():
  print("Vehicles available for booking: ")
  for i in range(len(vehicles)):
    print(f"{i+1}. {vehicles[i][0]} ({vehicles[i][1]} seats) (In Stock {vehicles[i][2]})")

def book_vehicle():
    display_vehicles()
    keep_asking = True
    while keep_asking:
        try:
            vehicle_choice = int(input("Enter the number of the vehicle you want to book: "))
            keep_asking = False
        except ValueError:
            print("Please enter a valid input")
    if vehicle_choice < 1 or vehicle_choice > len(vehicles):
        print("Invalid choice. Please try again.")
        return
    vehicle = vehicles[vehicle_choice-1]
    if vehicle[2] == 0:
        print("Sorry, this vehicle is already booked.")
        return
    continue_asking = True
    while continue_asking:
        name = input("Enter your name: ")
        if name.strip(" ") == "":
            print("please enter a valid name")
        else:
            continue_asking = False

    bookings.append([vehicle[0], name])
    vehicle[2] -= 1
    print(f"Vehicle {vehicle[0]} booked for {name}.")

def end_of_day():
  print("End of day bookings:")
  for booking in bookings:
    print(f"{booking[0]} - {booking[1]}")
  bookings.clear()
  if len(bookings) == 0:
      print("There were no bookings today")

# Main loop
keep_asking = True
while keep_asking:
  print("1. Book a vehicle")
  print("2. End of day")
  choice = input("Enter your choice: ")
  if choice == "1":
    book_vehicle()
  elif choice == "2":
    end_of_day()
    keep_asking = False
  else:
    print("You have not entered a option please enter again")

