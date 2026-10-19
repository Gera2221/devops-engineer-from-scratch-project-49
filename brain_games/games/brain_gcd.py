from brain_games.logic import gcd
import random
import prompt


DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def get_logic():
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    correct_answer = gcd(number1, number2)

    question = (f'Question: {number1} {number2}')

    return question, correct_answer
