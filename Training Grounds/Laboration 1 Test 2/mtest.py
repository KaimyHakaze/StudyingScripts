def menu():
    name = input('Identification required, please comply: ')

    name_out = name.capitalize()

    output = f'User privilege granted, welcome {name_out}'

    print(output + '\n')

    run =  True
    stop = False

    print('1. Division\n 2. Guess\n')
    answer = int(input("Välj ett alternativ: "))
    choice = 0 + answer

    menu1 = 0
    menu2 = 0

    while (run):
        
        
        
        
        if(choice != menu):
            from numeric import selection as divide
            divide()
            break
            
        if (choice == 2):                
             from numeric import selection2 as guess
             guess()
             
        else: 
            stop = True
            run = False
    
    while(stop):
        print('Incorrect input')
        stop = int(input(' Enter 0 or 3 for:\n 0. Exit 1. Try again\n Selection: '))
        if stop == 1:
            answer = int(input('Försök igen.\n 1. Division 2. Guess\n Val: '))
            
        if stop == 0:
            raise SystemExit


    
menu()

