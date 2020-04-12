#### Książka adresowa:
#Program przechowujący danę kontaktowe znajomych/klientów.
#- Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
    #- Wyświetlenie wszystkich wpisów
    #- Stworzenie nowego wpisu (dane wczytywane z klawiatury)
    #- Usunięcie wpisu
    #- Zakończenie pracy programu
#- Program powinien na starcie mieć już wprowadzone kilka wpisów

import sys

# formatowanie - wyśrodkowanie tekstu
print('-' * 52)
print('{:^52s}'.format('KSIĄŻKA ADRESOWA - NUMERY KONTAKTOWE'))
print('-' * 52)
print('{:^52s}'.format('MENU'))
print('{:^52s}'.format('JEŻELI CHCESZ WYŚWIETLIĆ WSZYSTKIE WPISY WPISZ: ALL'))
print('{:^52s}'.format('JEŻELI CHCESZ STWORZYĆ NOWY WPIS WPISZ: NEW'))
print('{:^52s}'.format('JEŻELI CHCESZ USUNĄĆ WPIS WPISZ: DELETE'))
print('{:^52s}'.format('JEŻELI CHCESZ WYJŚĆ Z PROGRAMU WPISZ: EXIT'))
print('-' * 52)
print()

def koniec(): # - Zakończenie pracy programu
    if selection_user == 'exit':
        print('Dziękuję za skorzystanie z programu.')
        print('''   ***       
  ** **
 **   **
 **   **         **** 
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *
    ** **  ** **        **
    **   **  **
   *           *
  *             *
 *    0     0    *
 *   /   @   \   *
 *   \__/ \__/   *
   *     W     *
     **     **   
       *****
Bogatego zajączka, najlepszego ! :)
       ''') # wielkanocny akcent :)
        print('-' * 52)
        sys.exit(0)


def delete(): # - Usunięcie wpisu
    if selection_user == "delete":
        entry = input('Jaki wpis chcesz usunąć (podaj imie)? : ')
        entry_1 = entry.upper()
        friends_data.pop(entry_1)


def new(): # - Stworzenie nowego wpisu (dane wczytywane z klawiatury)
    if selection_user == 'new':
        name = input('Proszę o podanie imienia: ')
        number = input('Proszę o podanie numeru: ')
        name = name.upper()
        friends_data[name] = number


def all(): # - Wyświetlenie wszystkich wpisów
    if selection_user == 'all':
        print(friends_data)

# - Wprowadzone kilka wpisów
friends_data = {'ANNA' : '733270764', 'IWONA' : '633258974', 'STASIEK' : '477877985'}
print(f'KSIĄŻKA ADRESOWA: {friends_data}')

# nieskończona pętla wykonywana do momentu sys.exit(0)
while True:
    selection_user = input('Jaką czynność chcesz wykonać? ')
    selection_user = selection_user.lower()
    koniec()
    delete()
    new()
    all()
