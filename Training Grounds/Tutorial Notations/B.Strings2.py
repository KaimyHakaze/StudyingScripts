#Förvara strängar i variabler

ex_name = 'Kaimy'

print(ex_name)

#Exempel på kombinering utav strängar 

#Skapar en till sträng variabel då första redan är angiven ovan

exb_name = 'Vanir'

print(ex_name + exb_name)

#Exempel på kombination utav program definerad sträng 
print ('Hello ' + ex_name + ' ' + exb_name)




"""
ex_name + '' används då det skapar ett mellanrum, precis som mellanslaget efter Hello


Men eftersom ex_name är en funktion vi anropar krävs det att göra ett mellanrum på detta sätt


Användning utav funktioner för att modifiera strängar 

"""

citat = 'The demon they called Sora'

print(citat.upper()) #skriver skriver ut variabeln med stora bokstäver citat.lower det motsatta

print(citat.capitalize()) #skriver ut stor bokstav för det ord meningen börjar på

print(citat.count('e')) #räknar och skriver ut antal gånger angiven bokstav används


#Användar definerade inputs i kombination med exempel ovan

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

print ('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize() + '!')
