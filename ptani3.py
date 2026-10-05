nazev = input("Co kupuješ? ")
cena = float(input("Cena za kus (Kč): "))
pocet = int(input("Kolik kusů? "))

bez_dph = cena * pocet
sleva = bez_dph * 0.10
bez_dph -= sleva
dph = bez_dph * 0.21
s_dph = bez_dph + dph

print()
print("Položka:", nazev, "×", pocet)
print("Cena bez DPH:", bez_dph, "Kč")
print("DPH 21 %:", dph, "Kč")
print(f"Celkem k úhradě: {s_dph} Kč")
