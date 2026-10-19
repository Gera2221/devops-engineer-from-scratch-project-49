import prompt
import random


def main():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')


    counter = 0

    while counter < 3:
        number = random.randint(0,1000)
        print(f'Question: {number}')

        answer = prompt.string('Your answer: ')

        if int(number) % 2 == 0 and answer == 'yes':
            counter += 1
            print('Correct!')

        if int(number) % 2 != 0 and answer == 'no':
            counter += 1
            print('Correct!')

        if int(number) % 2 == 0 and answer != 'yes':
            print(f"Your answer is wrong ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            return
              
        if int(number) % 2 != 0 and answer != 'no':
            print(f"Your answer is wrong ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            return

    if counter == 3:
            print(f'Congratulations, {name}')
    

