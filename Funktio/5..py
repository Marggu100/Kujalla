def poista_parittomat (luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

def main():
    alkuperainen = [1, 4, 11, 15, 7, 10, 22, 2]
    print(f"alkuperäinen: {alkuperainen}")

    karsittu = poista_parittomat(alkuperainen)
    print(f"parittomat: {karsittu}")

if __name__ == "__main__":
    main()