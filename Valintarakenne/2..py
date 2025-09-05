#LUX = ("Parvekkeellinen hytti yläkannella")
#A = ("Ikkunallinen hytti autokannen yläpuolella")
#B = ("ikkunaton hytti autokannen yläpuolella")
#C = ("Ikkunaton hytti autokannen alapuolella")

print("LUX")
print("A")
print("B")
print("C")

hytti = input("kerro hyttiluokkasi: ")

if hytti == "LUX":
    print("Parvekkeellinen hytti yläkannella")
elif hytti == "A":
    print("Ikkunallinen hytti autokannen yläpuolella")
elif hytti == "B":
    print("Ikkunaton hytti autokannen alapuolella")
elif hytti == "C":
    print("Ikkunaton hytti autokannen alapuolella")

else:
    print("Emme löytäneet kyseistä luokkaa. Muistithan käyttää isoja kirjaimia")
