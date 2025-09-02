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
