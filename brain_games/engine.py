from brain_games.logic import greeting
import prompt


def run_game(game):
    name = greeting()

    print(game.DESCRIPTION)

    counter = 0

    while counter < 3:
        
        question, correct_answer = game.get_logic()
        print(question)
        answer = prompt.string('Your answer: ')

        if answer == str(correct_answer):
            counter += 1 
            print('Correct!')
        elif answer != str(correct_answer):
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return

    if counter == 3:
        print(f'Congratulations, {name}!')

        

    