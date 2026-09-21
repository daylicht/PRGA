import math
import time

znak = "O"        # zkus "*" nebo "●" — když spadne UnicodeEncodeError, terminál neumí unicode, vrať "O"
amplituda = 30
rychlost = 0.25
tlumeni = 0.02      # zkus 0 (netlumené), 0.05 (rychle dokmitá), 0.2

for krok in range(200):
    cas = krok * rychlost
    utlum = math.exp(-tlumeni * cas)            # klesá od 1 k 0
    vychylka = math.sin(cas) * utlum
    pozice = int(amplituda + amplituda * vychylka)
    print(" " * pozice + znak + " " * (2 * amplituda - pozice) + "|")
    print(utlum)
    time.sleep(0.04)
