import random 

# vaihdoin tiedotston nimeksi heitot, ei pystynyt importtaamaan väliviivaa

def heita(noppa: int):
    return [random.randint(1, 6) for _ in range(noppa)]

def nayta_nopat(nopat):
    print("Nopat:", " ".join(str(n) for n in nopat))

def pidettavat_nopat(nopat):
    print("Nykyiset nopat:", " ".join(str(n) for n in nopat))
    while True:
        valinta = input(" ").strip()
        if not valinta:
            return nopat
        try:
            valitut = list(map(int, valinta.split()))
            temp_nopat = list(nopat)
            for v in valitut:
                temp_nopat.remove(v)
            return valitut
        except (ValueError, IndexError):
            print("Yritä uudelleen")

def vuoro():
    nopat = heita(5)
    for heitto in range(2):
        nayta_nopat(nopat)
        valitut = pidettavat_nopat(nopat)
        if len(valitut) == 5:
            break
        uudet = heita(5 - len(valitut))
        nopat = valitut + uudet

    return nopat


