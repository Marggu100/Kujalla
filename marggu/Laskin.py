print("valitse mitä toimintoa haluat käyttää:\n a:yhteenlasku\n b:vähennyslasku\n c:jakolasku\n d:kertolasku")

valinta = input("valintasi (a-d):")

a = float(input("anna ensimmäinen luku "))
b = float(input("anna toinen luku "))

if valinta == "a":
    print("yhteenlasku", a + b)
elif valinta == "b":
    print("vähennyslasku", a - b)
elif valinta == "c":
    print("jakolasku", a / b)
elif valinta =="d":
    print("kertolasku", a * b)
else:
    print("virheellinen valinta")


