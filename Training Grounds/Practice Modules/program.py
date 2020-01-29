#En av mina program/run moduler som gjordes i lärosyfte, kan finnas rester av felaktig kod, modul ej menad för användning.

        

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
        while run == 0:        
                from numeric import selection2 as gissa 
                print(gissa)
                run = run+1
                break
            

def avsluta():

    if __name__ == "__main__": 
        print('Avlsutar')
        raise SystemExit



def welcome():
        
         
        name = input('Identification required, please comply: ')

        name_out = name.capitalize()

        output = f'User privilege granted, welcome {name_out}'
        print(output + '\n')

        stopnow = 1
        menyval = 0
        while (menyval !=1):

            Mainfunction = int(input('Välj ett alternativ\n 1. Dividering 2. Gissning\n 3. Avsluta Programmet.\n Ange val: '))
            if (Mainfunction == 1):
                from numeric import selection
                print(selection)
                break
            
            if (Mainfunction == 2):
                from numeric import selection2
                print(selection2)
                break
            if (Mainfunction == 3):
                menyval = menyval + 1
                break

            else:
                    Mainfunction = int(input('Incorrect input!\nVälj ett alternativ\n1. Dividering\n2. Gissning\n3. Avsluta \n Ange val: '))
                    break
        if menyval == stopnow: 
            raise SystemExit
welcome()