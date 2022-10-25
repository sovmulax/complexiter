import time


def tri_selection(tab):
    start = time.time_ns()
    for i in range(len(tab)):

       # Trouver le min
        min = i

        for j in range(i+1, len(tab)):
            if tab[min] > tab[j]:
                min = j

        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    end = time.time_ns()

    nano = format(end-start)
    nano_float = float(nano)
    print(" temps d'exécution : " + str(nano_float*0.000000001) + " s")

    return tab


tab = [20, 30, 15, 18, 7, 19, 21, 31, 81, 90]
print("Le tableau de base est: ")
print(tab)

tri_selection(tab)

print("Le tableau trié est: ")
print(tab)


