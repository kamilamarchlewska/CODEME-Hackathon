#Historyjka a'la RPG:

#Konieczność użycia modułu random.
#Program wypisuje kolejne "przygody" bohatera.
#Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami, np: "(bohater) poszedł do (miejsce)
# aby (czasownik)." może stać się "Jouxdrien II Niemrawy poszedł do tawerny aby zasnąć."
#Historyjka ma mieć zadaną długość i ma być możliwie losowa.


import random

# listy z których będą generowane dane
list_name = ['Marshkit', 'Whitestorm', 'Whitekit', 'Brindlekit', 'Henry', 'Lionheart ', 'Mousefur', 'Frostfur']
list_nickname = ['Great', 'Smelly', 'Big', 'Sexy', 'Crazy', 'Bright', 'Wild']
list_numeral = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
list_place = ['Icovaro', 'Pereplut', 'Peixe de Mar', 'Mag Turga', 'Mörhogg', 'Dreadfort', 'Casterly Rock']
list_verbs = ['rozkochał', 'zabił', 'uzdrowił', 'odczarował ', 'okradł', 'rozliczył', 'został zabity przez']


st = ('| RAPORT PODRÓŻY CZŁONKÓW GILDII "LEVENTROS" |')
width = len(st)
print('-' * width)
print(st)
print('-' * width)

name = random.choice(list_name)
nickname = random.choice(list_nickname)
numeral = random.choice(list_numeral)
place = random.choice(list_place)
verbs = random.choice(list_verbs)
print(f'{name} {numeral} {nickname} udał się do {place} gdzie {verbs} Druida Smargven.')

name = random.choice(list_name)
nickname = random.choice(list_nickname)
numeral = random.choice(list_numeral)
place = random.choice(list_place)
verbs = random.choice(list_verbs)
print(f'{name} {numeral} {nickname} teleportował się do {place} gdzie {verbs} Smoczycę Joannę.')

name = random.choice(list_name)
nickname = random.choice(list_nickname)
numeral = random.choice(list_numeral)
place = random.choice(list_place)
verbs = random.choice(list_verbs)
print(f'{name} {numeral} {nickname} podróżował do {place}. W trakcie podróży {verbs} Księżniczkę Satvę z Tarmond.')

name = random.choice(list_name)
nickname = random.choice(list_nickname)
numeral = random.choice(list_numeral)
place = random.choice(list_place)
verbs = random.choice(list_verbs)
print(f'{name} {numeral} {nickname} pojechał do {place} gdzie {verbs} szamankę Vintrev Esmont.')




