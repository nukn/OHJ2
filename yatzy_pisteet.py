
##### pisteiden tarkistus & kirjaus #####

pelaaja = {
    "ykköset": None, "kakkoset": None, "kolmoset": None,
    "neloset": None, "vitoset": None, "kutoset": None,
    "pari": None, "kaksi paria": None, "kolme samaa": None,
    "neljä samaa": None, "pieni suora": None, "iso suora": None,
    "täyskäsi": None, "sattuma": None, "yatzy": None
}


print(
f"""
-----pelaaja------
1 ykköset: {pelaaja['ykköset']}
2 kakkoset: {pelaaja['kakkoset']}
3 kolmoset:
4 neloset:
5 vitoset:
6 kutoset:

7 pari:
8 kaksi paria:
9 kolme samaa:
10 neljä samaa:
11 pieni suora:
12 iso suora:
13 täyskäsi:
14 sattuma:
15 yatzy:
-------------
""")



nopat = [1,1,1,1,1] 

print ('nopat:', nopat)
komento = input('mihin kirjataan? ')


def laske_pisteet(kohta, nopat):
    if kohta == "ykköset":
        return nopat.count(1) * 1
    elif kohta == "kakkoset":
        return nopat.count(2) * 2
    elif kohta == "kolmoset":
        return nopat.count(3) * 3
    elif kohta == "neloset":
        return nopat.count(4) * 4
    elif kohta == "vitoset":
        return nopat.count(5) * 5
    elif kohta == "kutoset":
        return nopat.count(6) * 6
    elif kohta == "sattuma":
        return sum(nopat)
    return 0

kohdat = list(pelaaja.keys())
try:
    komento = int(komento)
    kohta = kohdat[komento - 1]
    if pelaaja[kohta] is not None:
        print ("kohta on jo täytetty!")
    else:
        pisteet = laske_pisteet(kohta, nopat)
        pelaaja[kohta] = pisteet
        print(f"kirjattu pisteet kohtaan {kohta}")
except:
    print('virheellinen syöte')
    raise ValueError
    

    
#näytä päivitetty tulos
