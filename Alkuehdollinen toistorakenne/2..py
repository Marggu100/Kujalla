while True:
    tuumat = float(input("Tuumat, neg. luku lopettaa ohjelman: "))
    if tuumat < 0:
        print ("Ohjelma lopetetaan" )
        break
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on  {sentit:.2f} cm ")