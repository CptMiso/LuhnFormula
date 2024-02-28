#L'algorithme multiplie par deux un chiffre sur deux,
#en commençant par l'avant dernier et en se déplaçant de droite à gauche
#Si le double d'un chiffre est plus grand que neuf, il faut le ramener à un chiffre entre 1 et 9
#Soit on soustrait 9 au double. Avec le même exemple, 16 − 9 = 7.
#La somme de tous les chiffres obtenus est effectuée.
#Le résultat est divisé par 10. Si le reste de la division est égal à zéro, alors le nombre original est valide.

#numéro de la CB en chaine de caractere
cb = "972-487-086" # code valide
#cb = "972-487-123" #code non valide

#on remplace les caracteres indésirables
cb = cb.replace("-","")
#print(cb)

#création d'une liste vide pour la remplir des numéros de la CB pour pouvoir itérer dessus
cb_list_str=[]

#on remplit la liste vide
for p in cb:
    cb_list_str.append(p)

#print(cb_list)

#on inverse la list de la cb pour pouvoir itérer en partant de la droite pour aller à gauche
cb_list_str.reverse()

#print(cb_list_str)

#on créer une liste pair et impair
pair_list_str = cb_list_str[0::2]
#print(pair_list_str)
impair_list_str = cb_list_str[1::2]
#print(impair_list_str)

#transformation de la liste pair de chaine de caractere à integers pour pouvoir iterer et additionner
pair_list_int = [int(x) for x in pair_list_str]
#print(pair_list_int)
#transformation de la liste impair de chaine de caractere à integers pour pouvoir iterer et additionner
impair_list_int = [int(x) for x in impair_list_str]
#print(impair_list_int)


nv_list_cb_int = []

#on boucle sur la chaine integers impair pour faire le calcul et ensuite approvisionner la nouvelle liste
for i in impair_list_int:
    if i+i > 10:
        #print(i+i-9)
        nv_list_cb_int.append(i+i-9)
    else:
        #print(i+i)
        nv_list_cb_int.append(i+i)

#print(nv_list_cb_int)

#maintenant qu'on a le resultat on doit concatener 2 listes
nv_list_allcb_int = nv_list_cb_int + pair_list_int

#voici la liste entière sans l'ordonner puisque de toute facon on fait une full addition
#print(nv_list_allcb_int)

#addition des chiffres de la liste
somme = sum(nv_list_allcb_int)
#print(somme)

#modulo par 10 si reste = 0 alors valide sinon faux
if somme%10 == 0:
    print("Le code de carte bleue est valide")
else:
    print("Le code de carte bleue est faux")

    




