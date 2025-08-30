l = float(input("anna leivisköiden lukumäärä "))
n = float(input(" anna naulojen lukumäärä "))
lu = float(input("anna luotien lukumäärä "))
luotig = 13.3
naulag = 425.6
leig = 8512
paino = (lu * luotig) + (n * naulag) + (l * leig)
kg = paino / 1000
print(f"paino kiloina on {kg:.2f} kg")

