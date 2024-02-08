import random
import math

data = [['O', '0'], ['l', '1'], ['u', 'v']]
number_data = ['A', 'B', 'C', 'D', 'E']
level = 1
col = 5
row = 4


def start_message():
    print('Input cell number (e.g. A1) of the different character.')


def section_message():
    print('level: ' + str(level))


def view_question():
    choice_data = random.randint(0, 2)
    mistake_number = random.randint(0, (col * row) - 1)
    print('Debug: mistake_number = ' + str(mistake_number))
    question = data[choice_data]
    print(question)
    i = 0
    j = 0
    question_str1 = '/|'
    question_str2 = '--'
    while i < col:
        question_str1 += number_data[i] + ''
        question_str2 += '-'
        i += 1
    print(question_str1)
    print(question_str2)
    i = 0
    while i < row:
        question_str = str(i + 1) + '|'
        while j < col:
            if (i * col + j) == mistake_number:
                question_str += question[1]
            else:
                question_str += question[0]
            j += 1
        print(question_str)
        i += 1
        j = 0
    return mistake_number


def change_input_number(input_str):
    str_data = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                'E': 4}
    input_str_split = list(input_str)
    col_number = str_data[input_str_split[0]]
    row_number = int(input_str_split[1]) - 1
    input_number = row_number * col + col_number
    return input_number


def is_correct_number(mistake_number, input_number):
    if mistake_number == input_number:
        return True
    else:
        return False


def view_result(is_correct, mistake_number):
    if is_correct:
        print('Correct!')
    else:
        print('Wrong')
        print('Correct answer is ' + change_string(mistake_number))


def change_string(number):
    col_number = number % col
    row_number = math.floor(number / col) + 1
    string = number_data[col_number] + str(row_number)
    return string


def play():
    section_message()
    mistake_number = view_question()
    choice = input('(e.g. A1)')
    print('Debug: choice = ' + choice)
    input_number = change_input_number(choice)
    print('Debug: input_number = ' + str(input_number))
    is_correct = is_correct_number(mistake_number, input_number)
    view_result(is_correct, mistake_number)


start_message()
play()