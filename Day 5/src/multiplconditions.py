# Evaluate Conditions Using Logical Operators

has_id = input("Do you have valid id or not (yes/no)").strip().lower()
has_ticket = input("Do you have ticket to watch the movie (yes/no)").strip().lower()
age = input("Enter your age: ")

if age > 18 and has_id == "yes" and age >=18:
    print("You are eligible to enter the hall")
else: 
    print("You are not eligible to meet the all requirements")