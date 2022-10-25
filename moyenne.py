somme = 0
saisi = '0'
temp = 0
i = 0
while (saisi != '999'):
    saisi = input("voulez-vous saisir ? => ")
    if (saisi != '999'):
        temp = input("Entrez la note : ") 
        somme = somme + int(temp)
        i = i + 1
    else:
        try:
            print("la moyenne est : " + str(somme/i) + "/" + str(i))
        except ZeroDivisionError:
            moyenne = 0

# 1- 16,14 (G3); 
# 2- 15.84 (G1) ; 
# 3 -15,56 (G4); 
# 4- 15.42 (G5)
# 5- 14.64 (G2) ; 
