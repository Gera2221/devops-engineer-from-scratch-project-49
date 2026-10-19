import prompt
import random

def greeting():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a 

def random_progression():
    result = []
    start = random.randint(1,100)
    step = random.randint(2,15)

    result.append(start)

    index = 1

    for _ in range(1,10):
        current_element = start + index * step
        result.append(current_element)
        index +=1

    return result

def is_prime(number):
    if number < 2:
        return False
    for devider in range(2,number):
        if number % devider == 0:
            return False

    return True


