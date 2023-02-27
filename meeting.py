#!/usr/bin/env python3

attendees = ["Nicky", "Megan", "Amy"]
attendees.append("Paige")
attendees.extend(["Penny", "Dan"])
optional_guests = ["Mum", "Dad"]
potential_guests = attendees + optional_guests
print("There are", len(potential_guests), "potential attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_guests)
print("To:" + to_line)
print("CC:" + cc_line)
