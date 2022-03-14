#Exercice 1:
#Créer une fonction prenant 4 paramètres et les retournant en ordre croissant
#en utilisant que des conditions(en n’utilisant pas de loops).

def ordre(nb1, nb2, nb3, nb4):


    if (nb1 < nb2) and (nb3 < nb4):
        print(nb1, nb2, nb3, nb4)
    elif (nb1 > nb2) and (nb3 < nb4):
        print(nb2, nb1, nb4, nb3)
    return

ordre(54, 12, 45, 55)

