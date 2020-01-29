def selection(*divide):
    
    print('Enter two numbers to divide\n')
    NumOne = int(input('Select the first number: '))
    # NumOne = (int(NumberOne))    
            
    NumberTwo = input('Select an additional number: ')
    NumbTwo = (int(NumberTwo))

    results = (NumOne)
    divlist = []
    divlist.append(results)

    for value in range (1,1000):
        if((value%NumOne==0) and (value%NumbTwo==0)):
                divlist.append(value)
    print(f'{divlist}')
selection() 

def selection2(*random):
    from random import randint
        
    guess = int(input('Guess my number: ') ) 
    attempts = 0
    attList = []
    attList.append(attempts)

    machine = randint (1,100)
    while guess != machine:
        attempts = attempts + 1
        if guess > machine:
            guess = int(input('Too high, try again\n '))
            
        if guess < machine:
            guess = int(input('Too low, try again\n '))
    

    print (f'You are correct the answer was {machine} it took you {attempts} tries to get it right')
    
selection()
