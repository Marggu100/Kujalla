def laske_summa (luvut):
    return sum(luvut)

def main():
    luvut = [1, 2, 3, 4, 5]

    tulos = laske_summa(luvut)
    print((f"Listan {luvut} lukujen summaon {tulos}."))

if __name__ == "__main__":
    main()