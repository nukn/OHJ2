from heitot import vuoro
from pisteet import pelaaja, laske_pisteet, nayta_tulos

def kirjaus(pelaaja):
    nopat = vuoro()

    print ('lopulliset nopat:', nopat)
    komento = input('Mikä kohta taulukosta kirjataan? ')
    kohdat = list(pelaaja.keys())

    try:
        komento = int(komento)
        kohta = kohdat[komento - 1]
        if pelaaja[kohta] is not None:
            print ("Kohta on jo täytetty!")
        else:
            pisteet = laske_pisteet(kohta, nopat)
            pelaaja[kohta] = pisteet
            nayta_tulos(pelaaja)
            print(f"Kirjattu {pisteet} pistettä kohtaan {kohta}.\n")
    except:
        print('valitse väliltä 1-15')
        raise ValueError
    
        
def pelaajan_vuoro():
    print()
    print(f"KIERROS {kierros} / {kierrokset}")
    kirjaus(pelaaja)


if __name__ == "__main__":
    nayta_tulos(pelaaja)
    kierrokset = 15
    for kierros in range(1, kierrokset + 1):
        pelaajan_vuoro()
        
    print("Taulukko täytetty! lopullinen tulos:")
    print(nayta_tulos(pelaaja))