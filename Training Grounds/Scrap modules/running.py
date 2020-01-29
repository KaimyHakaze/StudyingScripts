def option1():
    option1 = 1
option1()

def option2():
    option2 = 2
option2()

def option3():
    option3 = 3
option3()

def option4():
    option4 = 4
option4()

def option5():
    option5 = 5
option(5)

def option6():
    option = 6
option(6)

def option7():
    option7 = 7
option7()

def option8():
    option8 = 8
option(8)

def option9():
    option9 = 9
option9()

def option10():
    
    option10 = 10
    namespace = 'Avsluta'
    thisis = f'{option10} {namespace}. : '
    print(thisis)

    
option10()

run = 1
stop = 0
while stop != 1:
    
    menu = int(input('Select an option: '))
    if menu == 0:
        print('Confirm Shutdown Request Y or N: ')