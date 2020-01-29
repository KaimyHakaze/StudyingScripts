# NumberOne = input('Select a number:')
# NumOne = (int(NumberOne))    
            
# NumberTwo = input('Select an additional number: ')
# NumbTwo = (int(NumberTwo))                

# for value in range (1,1000):
#     if((value%NumOne==0) and (value%NumbTwo==0)):                        
#         print(value)
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
        
        # if guess not in attList:
        #      attList.append(guess)
        
        # attempts = attempts +1
    if guess < machine:

        guess = int(input('Too low, try again: '))
        
        # if guess not in attList:
        #         attList.append(guess)
        # # attempts = attempts +1

# if guess not in attList:
#              attList.append(guess)
print (f'You are correct the answer was {machine} it took you {attempts} tries to get it right')
    

    # for answer in range (1,100):
    #     if machine_number < answer:
    #         lower = attempts+1 and (f'Try a lower number: {guessing}')
    #         return lower
            
    #     elif machine_number > answer:
            
    #         higher = attempts+1 and (f'Try a higher number: {guessing}')
    #         return higher

    #     elif machine_number==answer:
            
    #         right = (f'You are correct! It took you {attempts} tries') 
    #         return right
    #     else:
    #         incorrect = (f'Invalid input!') and (f'Try again: {guessing}')
    #         return incorrect