
import random

# Display 1st element of array in 3 * 3 formation

data = [['O','0'], ['l','1'], ['u','v']]
level = 1

def start_message():
  print('Input cell number (e.g. A1) of the different character.')

def section_message():
  print('level:' + str(level))

def view_question():
  choice_data = random.randint(0, 2)
  question = data[choice_data]
  print(question)

def play():
  section_message()
  view_question()
  choice = input('(e.g. A1)')
  print('Debug:choice = ' + choice)

start_message()
play()