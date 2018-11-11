import random
slova = ['ceruzka', 'slon', 'rybicka', 'slovnik'] # zatial berie iba male pismenka a slova, kde sa pismena neopakuju.

def vyhodnot(vyhodnot_pole, vyhodnot_slovo, neuspesny_pokus):
    "Vyhodnoti, ci sa este da hrat."
    if vyhodnot_pole == vyhodnot_slovo:
        return 'vyhra'
    elif neuspesny_pokus == 9:
        return 'prehra'
    else:
        return 'dalej'

def kresli(neuspesny_pokus):
    "Kresli sibenicu"
    if neuspesny_pokus == 0:
        with open('pokus0.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 1:
        with open('pokus1.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 2:
        with open('pokus2.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 3:
        with open('pokus3.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 4:
        with open('pokus4.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 5:
        with open('pokus5.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 6:
        with open('pokus6.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 7:
        with open('pokus7.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 8:
        with open('pokus8.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah
    elif neuspesny_pokus == 9:
        with open('pokus9.txt', encoding='utf-8') as subor:
            obsah = subor.read()
            return obsah


def hrame():
    "Zahra si s tebou sibenicu"
    slovo = random.choice(slova) #generuje slova zo zoznamu
    pole = len(slovo) * '-'
    pokus = -1 # pocita neuspesne pokusy, lokalna premenna
    while vyhodnot(pole, slovo, pokus) == 'dalej':
        while True:
            try:
                pismeno = str(input('Zadaj pismenko: '))
            except ValueError:
                print('Nezadala si pismeno. Znovu.')    #neriesi, ked len odenterujem a nic nezadam, vtedy sa mi skrati pole a uz to nedava zmysel
            else:
                if pismeno in slovo:
                    pole = pole[:slovo.index(pismeno)] + pismeno + pole[(slovo.index(pismeno) + 1):]
                elif pismeno not in slovo:
                    pokus = pokus + 1
                    print(kresli(pokus))
                print(pole)
                break
        else:
            break
    if vyhodnot(pole, slovo, pokus) == 'vyhra':
        print('Mas cele slovo, vyhrala si:)')
    elif vyhodnot(pole, slovo, pokus) == 'prehra':
        print(kresli(pokus))
        print('Smola')
    else:
        print('Nieco sa poruchalo')

hrame()
