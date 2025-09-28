import random

def peli ():
    numero = random.randint(1, 10)
    yritykset = 0

    print ("Tervetuloa peliin, tietokone arpoo luvun väliltä 1-10 " )
    while True:
        arvaus = input("arvaa luku väliltä 1-10 ").strip()
        if arvaus == "":
            print("Et arvannut mitään lukua, yritä uudelleen")
            continue
        try:
            a = int(arvaus)
        except ValueError:
            print("Anna oikea luku ")
            continue

        if a < 1 or a > 18:
            print("Arvaus pitää olla väliltä 1-10")
            continue
        yritykset += 1

        if a < numero:
            print("Liian pieni arvaus")
        elif a > numero:
            print("Liian suuri arvaus")
        else:
            print(f"Arvasit oikein! {numero} {yritykset} yrityksellä")
            break

if __name__ == "__main__":
    peli()