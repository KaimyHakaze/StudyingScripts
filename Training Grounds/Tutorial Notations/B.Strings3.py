name = input('What is your name boy? ')

# print('Hello there, ' + name.capitalize) 

""" 
print ovan markerad som comment för att minska mängd kod som körs,

nedan kommer exempel på formatering utav strängar

"""
name_out = name.capitalize()

output = f'Hello there, {name_out}' 

print(output)


"""
genom att använda sig utav f innan det man vill skriva ut det,
slipper man göra det på ett sätt man skulle behövt använda sig utav
om det var en äldre version av python än 3

Då behövs det göras på exempelvis följande sätt:

output = 'Hello there, { } '.format(name)

eller om flera strängar tas in från användaren kan man använda "måsvingar" antingen tomma,

för att skriva ut innehållet i den ordning det tas emot, eller specifierade


"""

