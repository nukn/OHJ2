
##### pisteiden tarkistus & kirjaus #####



pelaaja = {
    "ykköset": None, "kakkoset": None, "kolmoset": None,
    "neloset": None, "vitoset": None, "kutoset": None,
    "pari": None, "kaksi paria": None, "kolme samaa": None,
    "neljä samaa": None, "pieni suora": None, "iso suora": None,
    "täyskäsi": None, "sattuma": None, "yatzy": None
}
    

def nayta_tulos(pelaaja):
    i = 1
    yht = sum(v for v in pelaaja.values() if v is not None)
    
    print()
    print("---------[ YATZY ]-----------")
    for i, (kohta, arvo) in enumerate(pelaaja.items(), start=1):
        print (f"{i}: {kohta}: {arvo if arvo is not None else '-'}")
    print(f"Yhteensä: {yht}")
    print("------------------------------")
    print()


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
    elif kohta == "pari":
        # etsi mitä on väh. 2 ja palauta niistä suurin
        parit = []
        for luku in nopat:
            if nopat.count(luku) >= 2:
                parit.append(luku)
        if parit:
            return max(parit) * 2
    elif kohta == "kaksi paria":
        parit = []
        for luku in nopat:
            if nopat.count(luku) >= 2:
                parit.append(luku)
        if len(parit) >= 2:
            parit = set(parit)
            return sum(parit) * 2
    elif kohta == "kolme samaa":
        for luku in nopat:
            if nopat.count(luku) >= 3:
                return luku * 3
    elif kohta == "neljä samaa":
        for luku in nopat:
            if nopat.count(luku) >= 4:
                return luku * 4
    elif kohta == "pieni suora":
        if sorted(nopat) == [1, 2, 3, 4, 5]:
            return sum(nopat)
    elif kohta == "iso suora":
            if sorted(nopat) == [2, 3, 4, 5, 6]:
                return sum(nopat)
    elif kohta == "täyskäsi":
        pari = None
        kolmoset = None
        for luku in nopat:
            if nopat.count(luku) == 3:
                kolmoset = luku
            if nopat.count(luku) == 2:
                pari = luku
        if pari and kolmoset:        
            return sum(nopat)
    elif kohta == "sattuma":
        return sum(nopat)         
    elif kohta == "yatzy":
        if len(set(nopat)) == 1:
            return 50
        
    return 0


    
