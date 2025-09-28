oikeatunnus = "python"
oikeasalasana = "rules"

yritykset = 0
maxyritykset = 5

while yritykset < maxyritykset:
    tunnus = input("anna käyttäjätunnus: ")
    salasana = input("anna salasana: ")

    if salasana == oikeasalasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print("väärä salasana tai käyttäjätunnus")

else:
    print("pääsy evätty!")