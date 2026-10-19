from brain_games.logic import random_progression
import random
import prompt

DESCRIPTION = 'What number is missing in the progression?'

def get_logic():
    progression = random_progression()
    hidden_index = random.randrange(10)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = f'{" ".join(map(str, progression))}'

    return question, correct_answer
