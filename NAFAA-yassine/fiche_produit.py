#Mini-projet -Fiche produit

#premier produit
nom_produit = "Pommes Golden"
type_produit = "Fruit"
reference = "FR-POM-OO1"
poids_grammes = 750
date_fabrication = "2026-10-05"
date_limite_comsommation = "2026-10-12"
prix_kilo = 2.49

#2eme produit
nom_produit = "Yaourt nature"
type_produit = "Produit laitier"
reference = "PL-YAO-025"
poids_grammes = 125
date_fabrication = "2026-10-06"
date_limite_consommation = "2026-10-20"
prix_kilo = 3.20

print(type(nom_produit))
print(type(type_produit))
print(type(reference))
print(type(poids_grammes))
print(type(date_fabrication))
print(type(date_limite_comsommation))
print(type(prix_kilo))

poids_kg = poids_grammes / 1000

print(poids_kg)

print(f"Prix au kilo : {prix_kilo:.2f} €")

#Affichage fiche produit
print("="*40)
print("\t\tFICHE PRODUIT")
print("="*40)
print(f"Nom du produit : {nom_produit}")
print(f"Type du produit : {type_produit}")
print(f"Référence : {reference}")
print(f"Poids : {poids_kg:.2f}")
print(f"Date fabrication : {date_fabrication}")
print(f"Date limite de comsommation : {date_limite_comsommation}")
print(f"Prix au kilo : {prix_kilo:.2f}")
print("="*40)

#Prix

prix_produit = poids_kg * prix_kilo
print(f"{prix_produit:.2f} €")

#Afficher la référence avec sep , qui determine le separateur entre plusieurs chaine de caractere

print("PL" , "YAO" , "025" , sep="-")

"""Utiliser end , ici end determine le dernier caractere a la fin de la fonction print , ici ,c'est un espace , mais par
default , end est égal a \n"""

print("Nom du produit :" , end=" " )
print(nom_produit)

"""Questions de synthese
Question 1
Quel est le type de la variable :
poids_grammes = 750
Réponse : Integer

Question 2
Quel est le type de :
prix_kilo = 2.49
Réponse : Float

Question 3
Pourquoi la variable :
reference = "FR-POM-001"
est-elle une chaîne de caractères et non un nombre ?
Réponse ; Car il y a des lettres et des caractère spéciaux

Question 4
Quelle opération permet de convertir les grammes en kilogrammes ?
Réponse : Le poids en grammes divisé par 1000

Question 5
Quelle est la différence entre :
+
utilisé avec des nombres et :
+
utilisé avec des chaînes de caractères ?
Réponse : Avec un nombre , le plus est utilisé commme opérateur mathématique , tandis qu'avec une chaine de caractere ,
le + est utilisé pour la concaténation

Question 6
À quoi sert :
:.2f
Réponse : cela sert a définir le nombre de chiffres après la virgule que l'on veut afficher

Question 7
À quoi sert le paramètre :
sep
dans print() ?

Réponse : c'est un paramètres qui permet de définir un séparateur entre chaque valeurs affichées par la fonction print()

Question 8
À quoi sert le paramètre :
end
dans print() ?
Réponse : end determine le dernier caractere a la fin de la fonction print , mais par
default , end est égal a \n
"""
