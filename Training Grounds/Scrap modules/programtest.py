

        

def dela():
    if __name__ == "__main__": 
    
    
        run = 0
        while (run == 0):
            run = run +1
            from numeric import selection as divide                
            print(divide)
        
        if run != 0:
            
            print()
            
    

def guess():
    if __name__ == "__main__":
        
        

        run = 0
        while (run == 0):
               
            
            from numeric import selection2 as gissa 
            print(gissa)
            run = run +1
                
            
            

def avsluta():

    if __name__ == "__main__": 
        print('Avlsutar')
        raise SystemExit



def welcome():
        
         
        name = input('Identification required, please comply: ')

        name_out = name.capitalize()

        output = f'User privilege granted, welcome {name_out}'
        print(output + '\n')

        menyval = {
        1: dela,
        2:  guess,
        3:  avsluta,
        }
        Mainfunction = 0
        while (Mainfunction !=3):
            if (Mainfunction == 0):

                
                Mainfunction + 1
                Mainfunction = int(input('Välj ett alternativ\n 1. Dividering 2. Gissning\n 3. Avsluta Programmet.\n Ange val: '))
                

            elif (Mainfunction >= 1) and (Mainfunction < 3):
                    menyval[Mainfunction]()

            else:
                    Mainfunction = int(input('Incorrect input!\nVälj ett alternativ\n1. Dividering\n2. Gissning\n3. Avsluta \n Ange val: '))

welcome()