'''User Inputs their team name and opponents names, then inputs
results of the games then code prints out how many competition points the user now has'''


print("Welcome to the tournament! Please enter the name of your team and the names of your opponents.")
#get team name, check the user does not input any blanks
keep_team = True
while keep_team:
    team_name = input("please enter your teams name:")
    if team_name.strip(" ") ==  "":
        print("invalid name")
    else:
        keep_team = False

#lists to store opponent names and competition points
opponents = []
results = []

#while loop so the user does not input any blanks
keep_asking = True
while keep_asking:
    opponent_name = input("Enter the name of an opponent (or 'done' to finish): ")
    #checks wether or not word done has been entered
    if len(opponents) == 0 and opponent_name == "done":
        confirmation = input("You have not entered anything are you sure you want to continue? ")
        if confirmation.lower == "yes":
            keep_asking = False
        else:
            print("Then please make sure to enter a opponent name before entering done")
    elif opponent_name == "done":
        keep_asking = False
    else:
        if opponent_name.strip(" ") ==  "":
            print("invalid name")
        else:
            opponents.append(opponent_name)


count = 0
#for loop to ask the scores
for opponent in opponents:
    #first get your score, check it is a valid integer
    keep_going = True
    while keep_going:
        try:
            print(f"{team_name} vs {opponents[count]}")
            your_score = int(input("Enter your score: "))
            keep_going = False
        except ValueError:
            print("please enter a valid number")
    #get opponent score
    continue_asking = True
    while continue_asking:
        try:
            opponent_score = int(input("Enter your opponents score: "))
            continue_asking = False
        except ValueError:
            print("please enter a valid number")
    #checks wether or not your score is greater less or equal than the opponents
    # calculate result and add points to results list
    if your_score > opponent_score:
        results.append(3)
    elif your_score < opponent_score:
        results.append(1)
    elif your_score == opponent_score:
        results.append(2)
    count =+ 1
#sums up all the results inside the results list
total_points = sum(results)
#prints your team name and the total competition points your team earned
print(f"{team_name} has earned {total_points} competition points.")
