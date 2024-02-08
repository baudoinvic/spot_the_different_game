import random

data = [['O','0'], ['l','1'], ['u','v']]
level = 1

def start_message():
  print('Input cell number (e.g. A1) of the different character.')

def section_message():
  print('level: ' + str(level))

def view_question():
  choice_data = random.randint(0, 2)
  mistake_number = random.randint(0, 8)
  print('Debug: mistake_number = ' + str(mistake_number))
  question = data[choice_data]
  print(question)
  i = 0
  j = 0
  print('/|ABC')
  print('-----')
  while i < 3:
    question_str = str(i + 1) + '|'
    while j < 3:
      if (i * 3 + j) == mistake_number:
        question_str += question[1]
      else:
        question_str += question[0]
      j += 1
    print(question_str)
    i += 1
    j = 0

def play():
  section_message()
  view_question()
  choice = input('(e.g. A1)')
  print('Debug: choice = ' + choice)

start_message()
play()