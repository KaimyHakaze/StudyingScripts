
name = input('Identification required, please comply: ')

name_out = name.capitalize()

output = f'User privilege granted, welcome {name_out}'

print(output)

menu = input('Please choose desired function:\n 1. Divide\n 2. Guessing Game ')

user = (int(menu))
pc = 0
choice = (user+pc)

for choice in range(1,2):
        
    if choice == 1:
        from numeric import selection
        print(selection)
        
    elif choice == 2:
        from numeric import selection2
        print(selection2)

# select = int(input('Please choose desired function:\n 1. Divide\n 2. Guessing Game '))
 # for select in range(1,2):
    
#     if select is 1:
#         from numeric import selection
    
#     if select is 2:
#         from numeric import selection2
        

# select= int(input('Incorret entry, either enter 1 or 2:'))
    



# (f'{menu}')
# main()





