#!/usr/bin/python
import os
import sys

# Change to path containing the vcf files
path = '/home/void/.contacts/contacts/'
# Define the add_contact function
# TODO: Make Function more pythonic
def add_contact():
    with os.scandir(path) as folder:
        # Save contact as name.vcf
        with open(path+f"{name}.vcf", "w") as f:
            f.write(f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nN:\
                    {name};;;;\nTEL:{number}\nEMAIL:{email}\nEND:VCARD\n")


# Check if email was passed as argument, else ask for it.
try:
    email = sys.argv[1]
except:
    email = input("Please enter email:")

# Ask user for name and number
name = input("Please enter name:")
number = input("Please enter number:")
add_contact()
