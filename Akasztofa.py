import random
szo = ["hal","madár","teherautó", "számítógép", "egér", "talicska","laptop","billentyűzet" ]
randszo = (random.choice(szo)).lower()
hossz = len(randszo)
hiba = 0
kitalaltKar = 0
rejtettSzo = []
for i in range(0, hossz):
    rejtettSzo.append('_')
abc = ["a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "o", "ó", "ö", "ő", "p", "r", "s", "t", "u", "ú", "ü", "ű", "v", "z", "á", "é", "i", "í", "ó", "ö", "ő", "ú", "ü", "ű"]
        
while True:
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
    print("\nHibák száma: {}".format(hiba))
    if "_" not in rejtettSzo:
        print(f"Nyertél, a szavad: {randszo}")
        break
    if hiba == 9:
        print("   ___  ")
        print("  /   | ")
        print(" Ő    | ")
        print("<[]>  | ")
        print(" ||   | ")
        print("     <=>  ")
        break