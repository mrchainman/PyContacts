#!/usr/bin/python
import os
import fnmatch
import curses
import curses.textpad
import cursesmenu
import cursesmenu.items
import pyperclip
import sys


# Change with path to directory containing the .vcf files
path = '/home/void/.contacts/contacts'

# Read in vcf cards into a dictionary with pattern matching,
# conatining Name, Number and Email.
def contact_update():
    d = {}
    d.clear()
    with os.scandir(path) as folder:
        for entry in folder:
            with open(entry.path, "r")as f:
                line = f.readlines()
                # Set variables to prevent error.
                name = 'None'
                number = 'None'
                email = 'None'
                # If the variables are set, give them the new value.
                for i in set(line):
                    if i[0:2] == 'FN':
                        name = i.replace('FN', '').replace(':', '')\
                            .replace(';', '').replace('\n', '')\
                            .replace('CHARSET=UTF-8', '')
                    if i[0:3] == 'TEL':
                        number = i.replace(':', '').replace(';', '')\
                            .replace('\n', '').replace('TEL', '')
                    if i[0:5] == 'EMAIL':
                        email = i.replace(':', '').replace(';', '')\
                            .replace('\n', '').replace('EMAIL', '')\
                            .replace('TYPE=home', '')
                    if name not in d.keys():
                        d[name] = (entry.name, number, email)
    return d

# Ask for user input to search for a contact


def main():
    # Setup the curses window
    # TODO: Make it prettier
    stdscr = curses.initscr()
    curses.noecho()
    max_y, max_x = stdscr.getmaxyx()
    textfield = curses.newwin(5, 5, int(max_y/2 + 5), int(max_x/2 - 10))
    textbox = curses.textpad.Textbox(textfield)
    textbox.edit()
    name = textbox.gather()
    curses.endwin()
    return name

# Search for the given name, including names containg it and greate a list
def search_name(name, d):
    # Check if name was passed as an argument
    try:
        name = sys.argv[1]
    # Else set it to the name variable
    except:
        name = name
        name = name.replace(' ', '').replace('\n', '')
    pattern = f"*{name}*"
    matching = fnmatch.filter(d.keys(), pattern)
    contacts = []
    for i in matching:
        contacts.append(i)
    index = cursesmenu.SelectionMenu.get_selection(contacts)
    chosen = contacts[index]
    return chosen

# show the relevent data and copy the selected entry to clipboard
def show_data(key, d):
    stdscr = curses.initscr()
    stdscr.clear()
    stdscr.refresh()
    curses.noecho()
    # max_y, max_x = stdscr.getmaxyx()
    # data = curses.newwin(10, 10, int(max_y/2), int(max_x/2 - 10))
    infos = [key, d[key][1], d[key][2]]
    index = cursesmenu.SelectionMenu.get_selection(infos)
    to_copy = infos[index]
    pyperclip.copy(to_copy)

# Main Loop


# Start main
if (__name__ == "__main__"):
    dictionary = contact_update()
    name = main()
    key = search_name(name, dictionary)
    show_data(key, dictionary)
