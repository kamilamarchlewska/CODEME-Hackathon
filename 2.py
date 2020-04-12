#Generator imienia dla Wojownika RPG:

#Konieczność użycia modułu random.
#Program generuje wymawialne(!) imię o zadanej długości i dodaje do niego przydomek (opcjonalnie również tytuł i liczebnik). Np. 'Jouxdrien II Niemrawy'.
#Pomysł jest zainspirowany grą: http://progressquest.com/play/main.html
#Imię musi zaczynać się od wielkiej litery.
#Program można kontynuować używając pomysłu poniżej.

import random
# listy z których będą generowane dane
list_name = ['marshkit', 'whitestorm', 'whitekit', 'brindlekit', 'henry', 'lionheart ', 'mousefur', 'frostfur']
list_nickname = ['Great', 'Smelly', 'Big', 'Sexy', 'Crazy', 'Bright', 'Wild']


sign = '|Generator imienia dla Wojownika RPG|'
width = len(sign)
print('.' * width)
sign_1 = sign.upper()
print(sign_1)
print('.' * width)

# losowanie
a = random.choice(list_name)
a = a.capitalize() # imię zaczyna się od wielkiej litery
b = random.choice(list_nickname)

# formatowanie - wyśrodkowanie tekstu
print('{:^38s}'.format(a))
print('{:^38s}'.format(b))
print('.' * width)