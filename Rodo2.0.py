imie = input("Prosze podaj swoje imie\n, moj przyjacielu $")
nazwisko = input("Prosze podaj swoje nazwisko\n, moj przyjacielu $")
try:
    wiek = int( input("Podaj swoj wiek"))
except ValueError as cos_poszlo_nie_tak:
    wiek = 8
    print(f'wiek ustawiono na {wiek},\nwystapil {cos_poszlo_nie_tak}')
numerKarty = input("Potrzebuje numer twojej karty,\n aby wysłać ci zaliczke za tone zlota")
kodCVC = input("Prosze podac kod CVC, Nie martw sie\n, zostanie to bezpiecznie zapisane")