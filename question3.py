import random

# Use random int

level = 1

def start_message():
    print('Input cell number (e.g. A1) of the different character.')

def section_message():
    print('level:' + str(level))

def play():
    section_message()
    choice = input('(e.g. A1) ')
    print('Debug:choice = ' + choice)

start_message()
play()
