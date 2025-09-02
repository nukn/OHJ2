
##### pisteiden tarkistus & kirjaus #####

pelaaja = {
    "ykköset": None, "kakkoset": None, "kolmoset": None,
    "neloset": None, "vitoset": None, "kutoset": None,
    "pari": None, "kaksi paria": None, "kolme samaa": None,
    "neljä samaa": None, "pieni suora": None, "iso suora": None,
    "täyskäsi": None, "sattuma": None, "yatzy": None
}


def nayta_tulos(pelaaja:dict):
    i = 1
    yht = sum(v for v in pelaaja.values() if v is not None)
    print()
    print("---------pelaaja----------")
    for i, (kohta, arvo) in enumerate(pelaaja.items(), start=1):
        print (f"{i}: {kohta}: {arvo if arvo is not None else '-'}")
    print(f"Yhteensä: {yht}")
    print("---------------------------")
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
    elif kohta == "sattuma":
        return sum(nopat)
    return 0


    



