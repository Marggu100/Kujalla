luvut = []

while True:
    syote = input("Anna luku? ")
    if syote == "":
        break
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Anna uusi numero? ")

luvut.sort(reverse=True)

print("\nViisi suurinta lukua:")
for luku in luvut [:5]:
    print(luku)