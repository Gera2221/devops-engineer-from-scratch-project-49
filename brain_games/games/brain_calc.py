import random



DESCRIPTION = 'What is the result of the expression?'

def get_logic():
    operation = random.choice(['*','-', '+'])
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    
    question = (f'Question: {number1} {operation} {number2}')
    
    if operation == '*':
        correct_answer = number1 * number2
    elif operation == '-':
        correct_answer = number1 - number2
    elif operation == '+':
        correct_answer = number1 + number2
    

    return question, correct_answer