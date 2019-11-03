from random import randint

x = randint(1, 11)
liczba_prob = 1

print('Została wylosowana liczba z zakresu 1-10. Zgadnij ją!')

y = input('Podaj liczbę: ')

while y != "exit":
    y = int(y)
    if x > y:
        print('Podana liczba jest za mała!')
        y = input('Podaj większą liczbę: ')
        liczba_prob += 1
        continue
    elif x < y:
        print('Podana liczba jest za duża!')
        y = input('Podaj mniejszą liczbę: ')
        liczba_prob += 1
        continue
    elif x == y:
        print(f"Trafiłeś! Udało się w {liczba_prob} próbie!")
        break
    else:
        break
