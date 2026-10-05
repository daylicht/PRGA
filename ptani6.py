import random

hod = random.randint(1, 6)
print("Hodil jsem kostkou. Hádej, co padlo.")
tip = int(input("Tvůj tip (1 až 6): "))

print("Padlo:", hod)
print("Trefil ses:", tip == hod)
print("Tipoval jsi víc:", tip > hod)
print("Jsi daleko:", abs(tip - hod) > 2)
