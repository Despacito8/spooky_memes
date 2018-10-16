import random
wybur=input('wybierz kamien(K), papier(P), nozyce(N)\n')

komputer = random.choice( ['P', 'K', 'N'] )

if wybur == "N" and komputer == 'N':
    print ('remis')
if wybur == "N" and komputer == 'K':
    print ('przegrana')
if wybur == "N" and komputer == 'P':
    print ('wygrana')
if wybur == "P" and komputer == 'P':
    print ('remis')
if wybur == "P" and komputer == 'N':
    print ('przegrana')
if wybur == "P" and komputer == 'K':
    print ('wygrana')
if wybur == "K" and komputer == 'P':
    print ('przegrana')
if wybur == "K" and komputer == 'K':
    print ('remis')
if wybur == "K" and komputer == 'N':
    print ('wygrana')


