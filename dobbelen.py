import random

dobbelstenen = int(input("Hoeveel dobbelstenen wilt u gooien? : "))
totaalAantalGegooid = int(0)
i = 0

for i in range(dobbelstenen):
    
    aantalGegooid = random.randint(1, 6)
    print("Dobbelsteen wordt nu gerolt...")
    print("Gerolt: ", aantalGegooid)

    totaalAantalGegooid += aantalGegooid

    i += 1

    if i == dobbelstenen:
        print("Totaal gerolt: ", totaalAantalGegooid)
