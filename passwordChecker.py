#!/usr/bin/env python3

import sys

MASTER_PASSWORD = 'openup'

password = input("Please enter the super secret password:  ")
attempt_count = 1
while password != MASTER_PASSWORD:
        if attempt_count > 3:
                sys.exit("To many invalid password attempts")
        password = input("invalid password, try again:  ")
        attempt_count += 1
print("Welcome to secret town")