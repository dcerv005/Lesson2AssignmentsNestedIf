#Question 1 Task 1: Code Correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass #This is for task 3
elif place == "cave":
    print("You find a hidden treasure!")
    #Question 1 Task 2: Setting the Scene
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Great you can shine the path!")
    elif action == "proceed in the darkness":
        print("Be careful!")
    else:
        pass #This is for task 3
#Quesstion 1 Task 3: Default Path
else:
    pass
