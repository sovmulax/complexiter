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

# 1- 17,23 (G3); 
# 2- 16,90 (G4); 
# 3- 15,81 (G2) ;  
# 4- 15.16 (G1) ;
