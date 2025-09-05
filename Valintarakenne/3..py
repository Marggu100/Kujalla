sukupuoli = input("Kerro sukupuolesi\nMies\nNainen\n_")
hemoglobiini = int(input("Kerro hemoglobiini arvosi: "))

if sukupuoli == "Mies":
    if hemoglobiini < 134:
        print("Hemoglobiinisi on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiinisi on korkea")
    else:
        print("Hemoglobiinisi on normaali")
elif sukupuoli == "Nainen":
    if hemoglobiini < 117:
        print("Hemoglobiinisi on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiinisi on korkea")
    else:
        print("Hemoglobiinisi on normaali")
else:
    print("Virheellinen sukupuoli, kirjoita `Mies´ tai ´Nainen`")

