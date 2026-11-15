from brain_games.logic import is_even
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_logic():
    number = random.randint(1,1000)
    question = f'Question: {number}'
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer