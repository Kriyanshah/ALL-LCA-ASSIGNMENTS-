# Assignment 5

import re

string = input("Enter a string: ")

if re.fullmatch(r'[a-zA-Z0-9]+', string):
    print("String contains only allowed characters.")
else:
    print("String contains invalid characters.")