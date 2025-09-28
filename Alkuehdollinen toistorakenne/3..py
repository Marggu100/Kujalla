luvut = []

while True:
    put = input("Anna luku, tyhjä lopettaa ohjelman: ")
    if put == "":
        break
    try:
        luku = float (put)
        luvut.append (luku)
    except ValueError:
       print("Anna kelvollinen numero")

if len(luvut) > 0:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin kuku: {max(luvut)}")
else:
    print("Et antanut yhtään lukua")