import math

def laske_yksikkohinta(halkaisija_cm, hinta):
    halkaisija_m = halkaisija_cm / 100
    sade = halkaisija_m / 2
    pinta_ala = math.pi * sade**2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

def main():
    print("Syötä ensimmäisen pizzan mitat: ")
    halkaisija1 = float(input("Halkaisija (cm): "))
    hinta1 = float(input("Hinta (€): "))

    print(("\n.Syötä toisen pizzan mitat: "))
    halkaisija2 = float(input("Halkaisija (cm): "))
    hinta2 = float(input("HInta (€): "))

    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    print(f"\nEnsimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m^2")
    print(f"Toisen pizzan yksikköhinta {yksikkohinta2:.2f} €/m¨^2")

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahoille")
    elif yksikkohinta1 < yksikkohinta2:
        print("Toinen pizza antaa paremman vastineen rahoille")
    else:
        print("Molemman pizzat ovat yhtä hyviä vaihtoehtoja")

if __name__ == "__main__":
    main()