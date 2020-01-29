def selection():

    NumberOne = input('Select a number:')
    NumOne = (int(NumberOne))    
            
    NumberTwo = input('Select an additional number: ')
    NumbTwo = (int(NumberTwo))
                 
    
    

    
    for value in range (1,1000):
        if((value%NumOne==0) and (value%NumbTwo==0)):
            
            print(value)
            
            


selection()


def selection2():
    
    
    
    from random import randint as machine_number
    machine_number = ((int)(1,100))
    guessing = input('Guess my number: ')  
    answer = (int(guessing))
    attempts = 1

    for answer in range (1,100):
        if machine_number < answer:
            lower = attempts+1 and (f'Try a lower number: {guessing}')
            return lower
            
        elif machine_number > answer:
            
            higher = attempts+1 and (f'Try a higher number: {guessing}')
            return higher

        elif machine_number==answer:
            
            right = (f'You are correct! It took you {attempts} tries') 
            return right
        else:
            incorrect = (f'Invalid input!') and (f'Try again: {guessing}')
            return incorrect
    
selection2()

# def menu():
#     Select = input('Division or Guessing?')
#     Selectedo = 1
#     Selecte = (int(Select)) and Selectedo+1
#     for Selecte in range (1,2):
#         if (Selecte==1):
#             print(selection)
#         elif(Selecte==2):
#             print(selection2)
#     else:
#         winput = f'Wrong input, try again: {Select}'
#         return winput

        

