numer = int(input("Wprowadź liczbę: "))

if numer % 2 == 0:
    print("Podałeś parzystą liczbę.")
else:
    print("Podałeś nieparzystą liczbę.")

if numer % 4 == 0:
    print("Hej ta liczba jest wielokrotnością 4!")


num_1, num_2 = map(int, input("Wprowadź dwie liczby: ").split())

if num_1 % num_2 == 0:
    print(f"Pierwsza liczba ({num_1}) dzieli się przez drugą liczbę ({num_2}) bez reszty")
else:
    print(f"Pierwsza liczba ({num_1}) nie dzieli się przez drugą liczbę ({num_2}) bez reszty")
