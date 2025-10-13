import random
maara = int(input("Kuinka monta noppaa heitetään? "))

summa = 0
for i in range(maara):
    heitto = random.randint(1, 6)
    print(f"Nopan {i+1} silmäluku: {heitto}")
    summa += heitto
print(f"Silmälukujen summa on {summa}.")