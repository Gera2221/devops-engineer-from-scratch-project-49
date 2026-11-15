import prompt

from brain_games.logic import greeting


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
        else:
            print(
    f"'{answer}' is wrong answer ;(. "
    f"Correct answer was '{correct_answer}'.\n"
    f"Let's try again, {name}!"
)
            return

    if counter == 3:
        print(f'Congratulations, {name}!')

        

    
