"""Validare CNP"""
import datetime

while True:
    CNP = input("Introduceti un CNP (0 = iesire): ")
    if CNP == "0":
        break
    if len(CNP) != 13:
        print("CNP invalid! Nu ati introdus un string de 13 cifre.")
        continue
    if not CNP.isdigit():
        print("CNP invalid! Nu ati introdus doar cifre.")
        continue

    S = int(CNP[0])
    AA = int(CNP[1:3])
    LL = int(CNP[3:5])
    ZZ = int(CNP[5:7])
    JJ = int(CNP[7:9])
    NNN = int(CNP[9:12])
    C = int(CNP[-1])

    if S == 0:
        print("CNP invalid! Prima cifra nu poate fi 0!")
        continue
    elif S == 3 or S == 4:
        AA += 1800
    elif S == 5 or S == 6:
        AA += 2000
    else:
        AA += 1900

    try:
        datetime.datetime(AA, LL, ZZ)
    except ValueError:
        print("CNP invalid! Data nasterii nu exista!")
        continue

    if 46 < JJ < 51 or JJ > 52 or JJ == 0:
        print("CNP invalid! Codul judetului nu exista!")
        continue
    if NNN == 0:
        print("CNP invalid! Cifrele de la 9 la 11 nu pot fi toate 0!")
        continue

    control = 0
    COD = "279146358279"
    for i in range(12):
        control += int(CNP[i]) * int(COD[i])  #formula cifra control
    control = control % 11
    if control == 10:
        control = 1

    if control != C:
        print("CNP invalid! Cifra de control nu corespunde!")
        continue

    print("CNP VALID")
