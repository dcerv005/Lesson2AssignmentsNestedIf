#Question 2 Task 1: Code Correction
attendees1 = input("Enter number of attendees: ")
attendees = int(attendees1) #change str to int
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Question 2 Task 2: Venue Selection
additional_facilities= "audio system" if attendees >100 else "projector"
print(additional_facilities)

#Question 2 Task 3: Catering Choices
meal_choice= input("Vegetarian food?(yes/no)")

print("Veggie Delight Caterers") if meal_choice == 'yes' else print("Gourmet Meals Caterers")