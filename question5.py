import random

# Display one different element in 3 * 3 formation

data = [['0','0'],['1','1'],['u','v']]

level = 1

def start_message():
     print('Input cell number (e.g. A1) of the different character.')

def section_message():
  print('level: ' + str(level))

def view_question():
  choice_data = random.randint(0, 2)
  question = data[choice_data]
  print(question)
  i = 0
  j = 0
  while i < 3:
    question_str = ''
    while j < 3:
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