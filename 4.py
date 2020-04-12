#Quiz
#Stwórz grę, która zawiera pytania z wiedzy ogólnej (Trivial pursuit)

s = '|QUIZ Z WIEDZY OGÓLNEJ|'
width = len(s)

result = 0

print('.' * width)
print(s)
print('.' * width)
print('Wpisz wybrany numer jako odpowiedź :)')
print()

print('Która epoka była wcześniej?')
print('(1) Oświecenie | (2) Barok')
question_first = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if question_first == 2 :
    result += 1

print()
print('Który prezydent objął urząd wcześniej?')
print('(1) Gabriel Narutowicz | (2) Ignacy Mościcki')
question_second = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if question_second == 2 :
    result += 1

print()
print('Co miało miejsce najpierw?')
print('(1) Odkrycie Ameryki przez Kolumba | (2) Hołd Pruski')
question_third = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if question_third == 1 :
    result += 1

print()
print('Co miało miejsce najpierw?')
print('(1) Odkrycie Ameryki przez Kolumba | (2) Hołd Pruski')
question_fourth = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if question_fourth == 1 :
    result += 1

print()
print('Kto pierwszy otrzymał nagrodę nobla?')
print('(1) Henryk Sienkiewicz | (2) Władysław Reymont')
question_fifth = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if question_fifth == 1 :
    result += 1

print()
print('Kto był koronowany wcześniej?')
print('(1) Władysław II Jagiełło | (2) Kazimierz III Wielki')
question_sixth = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if question_sixth == 2 :
    result += 1

print()
print('Kto zmarł wcześniej?')
print('(1) Elvis Presley | (2) Marilyn Monroe')
question_seven = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if question_seven == 2 :
    result += 1

print()
print('Kto pierwszy wprowadził powszechne prawo wyborcze dla kobiet?')
print('(1) Polska | (2) Francja')
question_eighth = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if question_eighth == 1 :
    result += 1

print()
print('Który film jest starszy?')
print('(1) Titanic | (2) Pianista')
question_ninth = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 1')
if question_ninth == 1 :
    result += 1

print()
print('Który zespół powstał wcześniej?')
print('(1) Qeen | (2) The Beatles')
question_tenth = int(input('► Wybieram: '))
print('► Prawidłowa odpowiedź: 2')
if question_tenth == 2 :
    result += 1

print()
if result >= 5:
    print(f'Twój wynik to: {result}. Gratuluję!')
else:
    print(f'Twój wynik to: {result}. Spróbuj ponownie :)')