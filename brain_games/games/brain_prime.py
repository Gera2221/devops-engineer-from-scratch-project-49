from brain_games.logic import is_prime
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def get_logic():
    number = random.randint(1,100)
    question = f'Question: {number}'
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
