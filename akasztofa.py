import random

zoldsegek = ["uborka", "paradicsom", "paprika", "káposzta", "saláta", "hagyma", "fokhagyma", "brokkoli", "karfiol", "krumpli", "édesburgonya", "répa", "retek", "tök", "bab", "padlizsán", "gomba", "újhagyma", "gyömbér", "torma", "spárga", "cukkini", "kukorica", "sóska", "borsó"]
gyumolcsok = ["alma", "dinnye", "banán", "barack", "szőlő", "sárkánygyümölcs", "kókusz", "ananász", "cseresznye", "meggy", "áfonya", "eper", "málna", "kiwi", "mangó", "papaja", "körte", "licsi", "gránátalma", "szilva", "citrom", "lime", "csillaggyümölcs"]
allatok = ["zebra", "zsiráf", "medve", "róka", "kutya", "macska", "nyúl", "ló", "bagoly", "egér", "veréb", "harkály", "cápa", "rája", "medúza", "elefánt", "ponty", "kapibara", "strucc", "emu", "béka", "farkas", "papagáj"]
hiba = 0
kitalaltKar = 0
rejtettSzo = []
abc = ["a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "o", "ó", "ö", "ő", "p", "r", "s", "t", "u", "ú", "ü", "ű", "v", "z", "á", "é", "i", "í", "ó", "ö", "ő", "ú", "ü", "ű"]

randszo = ""

jatekKezdet = False

print("--- AKASZTÓFA ---")

while jatekKezdet != True: 
    tema = int(input("Milyen témában szeretnél játszani? (Zöldségek - 1, Gyümölcsök - 2, Állatok - 3)\n")) 
    if tema == 1:
        randszo = random.choice(zoldsegek).lower()
        jatekKezdet = True
    elif tema == 2:   
        randszo = random.choice(gyumolcsok).lower()
        jatekKezdet = True
    elif tema == 3:
        randszo = random.choice(allatok).lower()
        jatekKezdet = True
    else:
        print("Nem megfelelő bemenet!")

hossz = len(randszo)

for i in range(0, hossz):
    rejtettSzo.append('_')

print(" ".join(rejtettSzo))

while jatekKezdet:
    betu = input("Kérek egy betűt: ").lower()
    if betu in randszo:
        iteracio = 0
        for i in randszo:
            if i == betu:
                rejtettSzo[iteracio] = betu
            iteracio+= 1
        iteracio= 0
        for i in range(0, hossz):
            print(rejtettSzo[iteracio], end=" ")
            iteracio += 1
        kitalaltKar += 1
        print("")
        if hiba==1:
            print("                         <=>  ")
        if hiba==2:
            print("                          | ")
            print("                         <=>  ")
        if hiba==3:
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==4:
            print("                          | ")
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==5:
            print("                       ___  ")
            print("                          | ")
            print("                          | ")
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==6:
            print("                       ___  ")
            print("                      /   | ")
            print("                          | ")
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==7:
            print("                       ___  ")
            print("                      /   | ")
            print("                     ő    | ")
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==8:
            print("                       ___  ")
            print("                      /   | ")
            print("                     ő    | ")
            print("                    <[]>  | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==9:
            print("                       ___  ")
            print("                      /   | ")
            print("                     Ő    | ")
            print("                    <[]>  | ")
            print("                     ||   | ")
            print("                         <=>  ")    

    else:
        iteracio= 0
        for i in randszo:
            if i == betu:
                rejtettSzo[iteracio] = betu
            iteracio+= 1
        iteracio= 0
        for i in range(0, hossz):
            print(rejtettSzo[iteracio], end=" ")
            iteracio+= 1
        hiba += 1
        print("")
        if hiba==1:
            print("                         <=>  ")
        if hiba==2:
            print("                          | ")
            print("                         <=>  ")
        if hiba==3:
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==4:
            print("                          | ")
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==5:
            print("                       ___  ")
            print("                          | ")
            print("                          | ")
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==6:
            print("                       ___  ")
            print("                      /   | ")
            print("                          | ")
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==7:
            print("                       ___  ")
            print("                      /   | ")
            print("                     ő    | ")
            print("                          | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==8:
            print("                       ___  ")
            print("                      /   | ")
            print("                     ő    | ")
            print("                    <[]>  | ")
            print("                          | ")
            print("                         <=>  ")
        if hiba==9:
            print("                       ___  ")
            print("                      /   | ")
            print("                     Ő    | ")
            print("                    <[]>  | ")
            print("                     ||   | ")
            print("                         <=>  ")           
    print()
    if "_" not in rejtettSzo:
        print(f"Nyertél, a szavad: {randszo}")
        break
    if hiba == 9:
        print(f"Vesztettél!\nA szó {randszo} volt.")
        break