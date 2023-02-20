#!/usr/bin/env python3

TICKET_PRICE= 10

tickets_remaining = 100

# Run this code continuosuly until we run out of tickets
while tickets_remaining >= 1:

	# Output how many tickets are remaining using the tickets_remaining variable

	print("There are {} tickets remaining".format(tickets_remaining))

	# Gather the users name and assign  it to a new variable

	name = input("Please enter your name:  ")

	# Promt the user by name and ask how many tickets they would like
	num_tickets = input("How many ticket's would you like {}?   ".format(name))
	# Expect a ValueError to happen and handle it approriatley 
	try:
		num_tickets = int(num_tickets)
		# Raise a ValueError if the request is for more tickets than are available
		if num_tickets > tickets_remaining:
			raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
	except ValueError as err:
		# Include the error text in the putput
		print("Ohh no, we ran into an issue. {} Please try again.".format(err))
	else:
		# Calculate the price (number of tickets * price) and assign it to a variable
		amount_due = num_tickets * TICKET_PRICE

		# Output the price to the screen

		print("The Total is £{}".format(amount_due))

		# Prompt user if they want to proceed Y or N?

		should_proceed = input("Do you want to proceed? Y or N  ")

			# If they want to proceed
		if should_proceed.lower() == "y":
			# print out to the screen "SOLD!" to confirm purchase
			# TODO Gather Credit Card information and process it
			print("SOLD!")
			#and the decrement the tickets remaining bu the number of tickets purchased
			tickets_remaining -= num_tickets
		#Otherwise...
		else:
			#Thank them by name
			print("Thank you {}".format(name))
			
# Notify when no more tickets left
print("Sorry the tickets are all sold out !!! :(")