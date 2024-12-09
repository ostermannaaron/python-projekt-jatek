import random

zoldsegek = ["uborka", "paradicsom", "paprika", "káposzta", "saláta", "hagyma", "fokhagyma", "brokkoli", "karfiol", "krumpli", "édesburgonya", "répa", "retek", "tök", "bab", "padlizsán", "gomba", "újhagyma", "gyömbér", "torma", "spárga", "cukkini", "kukorica", "sóska", "borsó"]
gyumolcsok = ["alma", "dinnye", "banán", "barack", "szőlő", "sárkánygyümölcs", "kókusz", "ananász", "cseresznye", "meggy", "áfonya", "eper", "málna", "kiwi", "mangó", "papaja", "körte", "licsi", "gránátalma", "szilva", "citrom", "lime"]
allatok = ["zebra", "zsiráf", "medve", "róka", "kutya", "macska", "nyúl", "ló", "bagoly", "egér", "veréb", "harkály", "cápa", "rája", "medúza", "elefánt", "ponty", "kapibara", "strucc", "emu", "béka", "farkas", "papagáj"]
orszag = ["argentína","belgium","magyarország","franciaország","lengyelország","spanyolország","horvátország","svédország","norvégia","finnország","oroszország","olaszország","szlovákia","szlovénia","csád","csehország","szerbia","ausztria","mexikó","peru","cyprus","törökország","izrael","japán","kína","usa","anglia","iraq","indonézia"]


ezoldsegek = ["cucumber", "tomato", "paprika", "salad", "onion", "broccoli", "carfiol", "potato", "sweetpotato", "carrot", "radish", "pumpkin", "bean", "eggplant", "mushroom", "ginger", "asparagus", "zukkini", "corn", "sorrel"]
egyumolcsok = ["apple", "melon", "banana", "peach", "grape", "dragonfruit", "coconut", "pineapple", "cherry", "blueberry", "strawberry", "raspberry", "kiwi", "mango", "papaya", "pear", "lychee", "pomegrante", "plum", "lemon", "lime"]
eallatok = ["zebra", "giraffe", "bear", "fox", "dog", "cat", "rabbit", "horse", "owl", "mouse", "sparrow", "woodpecker", "shark", "stingray", "medusa", "elephant", "carp", "capybara", "ostrich", "emu", "frog", "wolf", "parrot"]
eorszag = ["argentina","belgium","hungary","france","poland","spain","croatia","sweden","norway","finnland","russia","italy","szlovakia","slovenia","chad","serbia","austria","mexico","peru","cyprus","turkey","israel","japan","china","usa","britain","iraq","indonesia"]



hiba = 0
kitalaltKar = 0
rejtettSzo = []
abc = ["a", "á", "b", "c", "d", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "o", "ó", "ö", "ő", "p", "r", "s", "t", "u", "ú", "ü", "ű", "v", "z", "á", "é", "i", "í", "ó", "ö", "ő", "ú", "ü", "ű"]

randszo = ""
randomtema = "0"
ujra = True
jatekKezdet = False
nyelv=""
uj = True

if uj == True:
    while nyelv != "magyar" or nyelv != "english" and ujra == True:
        nyelv=input("Nyelv/language [Magyar/English]? ").lower()
        hiba = 0
        kitalaltKar = 0
        rejtettSzo = []
        jatekKezdet == True

        if nyelv == "magyar":    
            print("                                        \t\t   ------------- AKASZTÓFA -------------")
            print("                                        \t\t                Készítette:")
            print("                                        \t\tBognár Botond, Osztermann Áron, Lajkó Barnabás")
            print("\n")
            print("")
            print()
            while jatekKezdet != True: 
                tema = int(input("\n\n\nMilyen témában szeretnél játszani?\nZöldségek - 1\nGyümölcsök - 2\nÁllatok - 3\nOrszágok - 4\nBármilyen (nehéz) - 5\n")) 
                if tema == 1:
                    randszo = random.choice(zoldsegek).lower()
                    jatekKezdet = True
                elif tema == 2:   
                    randszo = random.choice(gyumolcsok).lower()
                    jatekKezdet = True
                elif tema == 3:
                    randszo = random.choice(allatok).lower()
                    jatekKezdet = True
                elif tema == 4:
                    randszo = random.choice(orszag).lower()
                    jatekKezdet = True
                elif tema == 5:
                    randomtema = random.randint(1,4)
                    if randomtema == 1:
                        randszo = random.choice(zoldsegek).lower()
                        jatekKezdet = True
                    elif randomtema == 2:
                        randszo = random.choice(allatok).lower()
                        jatekKezdet = True
                    elif randomtema == 3:
                        randszo = random.choice(gyumolcsok).lower()
                        jatekKezdet = True
                    elif randomtema == 4:
                        randszo = random.choice(orszag).lower()
                        jatekKezdet = True
                    
                else:
                    print("Nem megfelelő bemenet!")

            hossz = len(randszo)

            for i in range(0, hossz):
                rejtettSzo.append('_')

            print(" ".join(rejtettSzo))

            while jatekKezdet == True:
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
                elif len(betu) > 1:
                    print("Csak egy betűt tippelhetsz egyszerre!")
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
                    jatekKezdet = False
                    ujra = input("Szeretnél újra játszani? (i/n) ").lower()
                    if ujra == "n":
                        print("Vége a játéknak!")
                        ujra = False
                        jatekKezdet = False
                    elif ujra == "i":
                        ujra = True
                        jatekKezdet = False
                    else:
                        print("Nem megfelelő adat!")
                if hiba == 9:
                    print(f"Vesztettél!\nA szó {randszo} volt.")
                    jatekKezdet = False
                    ujra = input("Szeretnél újra játszani? (i/n) ").lower()
                    if ujra == "n":
                        print("Vége a játéknak!")
                        ujra = False
                        jatekKezdet = False
                    elif ujra == "i":
                        ujra = True
                        jatekKezdet = False
                    else:
                        print("Nem megfelelő adat!")







        if nyelv == "english":
            print("                                        \t\t   ------------- HANGMAN -------------")
            print("                                        \t\t                Made by:")
            print("                                        \t\tBognár Botond, Osztermann Áron, Lajkó Barnabás")
            print("\n")
            print("")
            print()
            while ujra == True:
                hiba = 0
                kitalaltKar = 0
                rejtettSzo = []
                while jatekKezdet != True: 
                    tema = int(input("\n\n\nWhat theme do you want to play?\nVegetables - 1\nFruits - 2\nAnimals - 3\nCountries - 4\nAnything (hard) - 5\n")) 
                    if tema == 1:
                        randszo = random.choice(ezoldsegek).lower()
                        jatekKezdet = True
                    elif tema == 2:   
                        randszo = random.choice(egyumolcsok).lower()
                        jatekKezdet = True
                    elif tema == 3:
                        randszo = random.choice(eallatok).lower()
                        jatekKezdet = True
                    elif tema == 4:
                        randszo = random.choice(eorszag).lower()
                        jatekKezdet = True
                    elif tema == 5:
                        randomtema = random.randint(1,4)
                        if randomtema == 1:
                            randszo = random.choice(ezoldsegek).lower()
                            jatekKezdet = True
                        elif randomtema == 2:
                            randszo = random.choice(eallatok).lower()
                            jatekKezdet = True
                        elif randomtema == 3:
                            randszo = random.choice(egyumolcsok).lower()
                            jatekKezdet = True
                        elif randomtema == 4:
                            randszo = random.choice(eorszag).lower()
                            jatekKezdet = True
                        
                    else:
                        print("Not right input!")

                hossz = len(randszo)

                for i in range(0, hossz):
                    rejtettSzo.append('_')

                print(" ".join(rejtettSzo))

                while jatekKezdet == True:
                    betu = input("I need a letter: ").lower()
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
                    elif len(betu) > 1:
                        print("You can only guess one letter!")
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
                        print(f"You won, your word is: {randszo}")
                        jatekKezdet = False
                        ujra = input("Do you want to play again? (y/n) ").lower()
                        if ujra == "n":
                            print("The game has ended!")
                            ujra = False
                            jatekKezdet = False
                        elif ujra == "y":
                            ujra = True
                            jatekKezdet = False
                        else:
                            print("Not right input!")
                    if hiba == 9:
                        print(f"You lost!\nThe word was: {randszo}")
                        jatekKezdet = False
                        ujra = input("Do you want to play again? (y/n) ").lower()
                        if ujra == "n":
                            print("The game has ended!")
                            ujra = False
                            jatekKezdet = False
                            break
                        elif ujra == "y":
                            ujra = True
                            jatekKezdet = False
                        else:
                            print("Not right input!") 
        if ujra == False:
            break