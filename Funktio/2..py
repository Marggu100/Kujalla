import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


def main ():
    tahkot = int(input("Anna nopan tahkojen määrä: "))
    silmaluku = 0

    while silmaluku != tahkot:
        silmaluku = heita_noppaa(tahkot)
        print(f"Heiton tulos: {silmaluku}")

if __name__ == "__main__":
    main()