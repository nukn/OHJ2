from heitot import vuoro
from pisteet import pelaaja, laske_pisteet, nayta_tulos


# tallenna kokonaistulos tiedostoon:
def tallenna_tulos(pelaaja):
    yht = sum(v for v in pelaaja.values() if v is not None)
    
    with open("tulokset.txt", "a") as tiedosto:
        tiedosto.write(f"{yht} \n")
        
# Paras tulos
kokonaistulos = tallenna_tulos(pelaaja) 

def paras_tulos():
    try:
        with open("tulokset.txt", "r") as tiedosto:
            tulokset = [int(rivi.strip()) for rivi in tiedosto if rivi.strip().isdigit()]
            return max(tulokset) if tulokset else 0
    except FileNotFoundError:
        return 0
    
paras = paras_tulos()

if kokonaistulos > paras:
    print(f"Uusi ennätys!: {kokonaistulos}")
else:
    print(f"Saavutettu tulos: {kokonaistulos}. Paras tulos on edelleen: {paras}")

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
    kierrokset = 2
    for kierros in range(1, kierrokset + 1):
        pelaajan_vuoro()
        
    print("Taulukko täytetty! lopullinen tulos:")
    nayta_tulos(pelaaja)
    tallenna_tulos(pelaaja)
    print("tulos tallennettu")
    
    # to do: näytä paras tulos, ilmoita jos uusi ennätys
