import random

from brain_games.logic import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_logic():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct_answer = gcd(number1, number2)

    question = (f'Question: {number1} {number2}')

    return question, correct_answer
