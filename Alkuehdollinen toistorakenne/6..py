import random

n = int(input("anna arvottavien pisteiden määrä: "))

osumat = 0

for _ in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        osumat += 1

pi_likiarvo = 4 * osumat / n
print(f"Piin likiarvo {n} pisteellä on: {pi_likiarvo}")
