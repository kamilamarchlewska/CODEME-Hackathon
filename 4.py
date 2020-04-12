#Quiz
#Stwórz grę, która zawiera pytania z wiedzy ogólnej (Trivial pursuit)

s = '|QUIZ Z WIEDZY OGÓLNEJ|'
width = len(s)

wynik = 0

print('.' * width)
print(s)
print('.' * width)
print('Wpisz wybrany numer jako odpowiedź :)')
print()

print('Która epoka była wcześniej?')
print('(1) Oświecenie | (2) Barok')
a = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if a == 2 :
    wynik += 1

print()
print('Który prezydent objął urząd wcześniej?')
print('(1) Gabriel Narutowicz | (2) Ignacy Mościcki')
b = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if b == 2 :
    wynik += 1

print()
print('Co miało miejsce najpierw?')
print('(1) Odkrycie Ameryki przez Kolumba | (2) Hołd Pruski')
c = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if c == 1 :
    wynik += 1

print()
print('Co miało miejsce najpierw?')
print('(1) Odkrycie Ameryki przez Kolumba | (2) Hołd Pruski')
d = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if d == 1 :
    wynik += 1

print()
print('Kto pierwszy otrzymał nagrodę nobla?')
print('(1) Henryk Sienkiewicz | (2) Władysław Reymont')
e = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if e == 1 :
    wynik += 1

print()
print('Kto był koronowany wcześniej?')
print('(1) Władysław II Jagiełło | (2) Kazimierz III Wielki')
f = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if f == 2 :
    wynik += 1

print()
print('Kto zmarł wcześniej?')
print('(1) Elvis Presley | (2) Marilyn Monroe')
g = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if g == 2 :
    wynik += 1

print()
print('Kto pierwszy wprowadził powszechne prawo wyborcze dla kobiet?')
print('(1) Polska | (2) Francja')
h = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if h == 1 :
    wynik += 1

print()
print('Który film jest starszy?')
print('(1) Titanic | (2) Pianista')
i = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if i == 1 :
    wynik += 1

print()
print('Który zespół powstał wcześniej?')
print('(1) Qeen | (2) The Beatles')
i = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if i == 2 :
    wynik += 1

print()
if wynik >= 5:
    print(f'Twój wynik to: {wynik}. Gratuluję!')
else:
    print(f'Twój wynik to: {wynik}. Spróbuj ponownie :)')