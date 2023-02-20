#!/usr/bin/env python3

first_name = input("Enter your first name:  ") # Asks the user to input their name

print( "Hello,", first_name) # Prints Hello including the first name input
if first_name == "Mike": # Checking if Mike is == Mike
    print(first_name, "is learning Python") # If correct Print Mike is learning Python
elif first_name == "Nicky":
    print(first_name, "Is learning with fellow students in the community! Good Job!")
else: # if first_name doesn't == Mike then promote learning python
    age = int(input("How old are you?  "))# asks the user to input their age
    if age <= 6: # if their age is less than or = to 6 then print check below
        print("Wow! You're {}. If you're confident with your reading already....".format(age) )
    print("You should definetley learn Python {}!".format(first_name)) # Prints the first_name of the person entered into the input {} set's the format which calls first_name
print("Have a nice day {}".format(first_name)) # print have a nice day to the same person
