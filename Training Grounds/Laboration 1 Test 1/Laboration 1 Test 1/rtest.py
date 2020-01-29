from random import randint
    
guess = int(input('Guess my number: ') ) 
attempts = 1
attList = []
attList.append(attempts)

machine = randint (1,100)
while guess != machine:
    attempts = attempts + 1
    if guess > machine:
        guess = int(input('Too high, try again: '))
    if guess < machine:
        guess = int(input('Too low, try again: '))

print (f'You are correct the answer was {machine} it took you {attempts} tries to get it right')
