import random

print("""
    +---------------------------------+
    |             HANG MAN            |
    +---------------------------------+
    |               |                 |
    |               |                 |
    |               O                 |
    |              /|\                |
    |               |                 |
    |              / \                |
    |         +----------+            |
    |         |          |            |
    +---------------------------------+
    |         Litere valabile         |
    +---------------------------------+
    |     A B C D E F G H I J K L M   |
    |     N O P Q R S T U V W X Y Z   |
    +---------------------------------+
    """)

x = [['istorie', 'matematica', 'filozofie', 'romana', 'engleza', 'muzica', 'informatica', 'geografie', 'fizica', 'religie'],
     ['pahar', 'lingurita', 'furculita', 'frigider', 'chiuveta', 'cutit', 'scaun', 'tirbuson', 'spatula', 'farfurie'],
     ['carne', 'mamaliga', 'branza', 'castravete', 'rosie', 'usturoi', 'cartofi', 'snitel', 'salata', 'miere'],
     ['variabila', 'functie', 'vecinatate', 'adunare', 'multime', 'derivata', 'integrala', 'probabilitate', 'serie', 'regresie'],
     ['vertebra', 'neuron', 'sinapsa', 'miocard', 'simptom', 'laringe', 'esofag', 'trahee', 'hemoglobina', 'epiteliu']]

print("""
    1 – Scoala
    2 – Obiecte
    3 – Mancare
    4 – Matematica
    5 - Biologie
    0 - Random
    """)
while True:
    a = input("Alegeti o optiune: ")
    if a.isdigit() and 0 <= int(a) <= len(x):
        a = int(a)
        if a == 0:
            a = random.randint(1, len(x))
        word = random.choice(x[a - 1])
        break
    else:
        print("Nu ati introdus o optiune valida! Reincercati.")

tries = 8
guess = []
wrong = ''
for i in range(len(word)):
    guess.append('_')

while tries > 0:
    print("".join(guess))
    char = input("Introduceti o litera: ")

    if len(char) != 1 or char.isdigit():
        print("Nu ati introdus o litera! Reincercati.")
        continue

    if char in guess or char in wrong:
        print("Ati introdus deja aceasata litera!")
        continue

    if char in word:
        for i in range(len(word)):
            if word[i] == char:
                guess[i] = char
        if '_' not in guess:
            break
    else:
        wrong += char
        tries -= 1
        print("Litera " + char + " nu se afla in cuvant! Incercari ramase: ", tries)

if tries == 0:
    print("GAME OVER")
else:
    print("Felicitari! Ati castigat!")

print("Cuvantul era: " + word)
