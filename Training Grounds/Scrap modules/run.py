name = input('Identification required, please comply: ')

name_out = name.capitalize()

output = f'User privilege granted, welcome {name_out}'
print(output + '\n')

stopnow = 0
# exitlist.append(stopnow)
running = 0

while (running !=1):

    repeatlist = (int(repeatlist))
    repeatlist.append(repeater)

    while (runtime != 1):
        repeatlist.append(repeater and (Mainfunction))
        Mainfunction = int(input('Välj ett alternativ\n 1. Dividering 2. Gissning\n 3. Avsluta Programmet.\n Ange val: '))
        stopnow = 0

    while (Mainfunction == 1) or (Mainfunction == 2) or (Mainfunction == 3) and (Repeater == 0) and (stopnow != 1):
        repeatlist.append(Mainfunction)
        if (Mainfunction == 1):
            from numeric import selection
            print(selection)
            repeatlist.append(Mainfunction)
            break
        
        if (Mainfunction == 2):
            from numeric import selection2
            print(selection2)
            repeater = repeater + 1
            break
        if (Mainfunction == 3):
                stopnow = stopnow +1
                break
        if (Repeater == 1):
        
            Mainfunction = int(input('Incorrect input!\nVälj ett alternativ\n1. Dividering\n2. Gissning\n3. Avsluta \n Ange val: '))
        if stopnow == 1: 
            raise SystemExit