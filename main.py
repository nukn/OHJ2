from heitot import vuoro
from pisteet import pelaaja, laske_pisteet, nayta_tulos


# tallenna kokonaistulos tiedostoon:
def tallenna_tulos(pelaaja):
    yht = sum(v for v in pelaaja.values() if v is not None)
    
    if yht:
        with open("tulokset.txt", "a") as tiedosto:
            tiedosto.write(f"{yht} \n")
        
    return(yht)



def kirjaus(pelaaja):
    nopat = vuoro()

    print ('Lopulliset nopat:', nopat)
    kohdat = list(pelaaja.keys())

    while True:
        komento = input('Mikä kohta taulukosta kirjataan? ')
        try:
            komento = int(komento)
            if 1 <= komento <= 15:
                kohta = kohdat[komento - 1]
                if pelaaja[kohta] is not None:
                    print ("Kohta on jo täytetty!")
                else:
                    pisteet = laske_pisteet(kohta, nopat)
                    pelaaja[kohta] = pisteet
                    nayta_tulos(pelaaja)
                    print(f"Kirjattu {pisteet} pistettä kohtaan {kohta}.\n")
                    break
            else:
                print('valitse väliltä 1-15')
        except ValueError:
            print("valitse väliltä 1-15")
  
    
        
def pelaajan_vuoro(pelaaja, kierros, kierrokset):

    print(f"KIERROS {kierros} / {kierrokset}")
    kirjaus(pelaaja)
    
    
def paras_tulos():
    try:
        with open("tulokset.txt", "r") as tiedosto:
            tulokset = [int(r.strip()) for r in tiedosto if r.strip().isdigit()]
        return max(tulokset) if tulokset else 0
    except FileNotFoundError:
        return 0


if __name__ == "__main__":
    
    nayta_tulos(pelaaja)
    kierrokset = 15
    for kierros in range(1, kierrokset + 1):
        pelaajan_vuoro(pelaaja, kierros, kierrokset)
        
    print("Taulukko täytetty! lopullinen tulos:")
    nayta_tulos(pelaaja)
    
    paras = paras_tulos()
    
    if sum(v for v in pelaaja.values() if v is not None) > paras:
        print("Uusi paras tulos!")
    else:
        print("Paras tulos:", paras)
        
    tulos = tallenna_tulos(pelaaja)