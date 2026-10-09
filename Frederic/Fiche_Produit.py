# assignation des variables


nom_produit = "Pommes Golden"
type_produit = "Fruit"
reference = "FR-POM-001"

poids_grammes = 750

date_fabrication ="2026/20/05"
date_limite = "2026-10-12"

prix_kg= 2.49
# calcul du poid
poids_kg = poids_grammes / 1000

print(f"poids : {poids_kg} kg ")

print(f"Prix au kilo : {prix_kg:.2f} €")


# affichage des  informations

print("="*51)
print(" "*17, "fiche produit")
print("="*51)
print("Nom du produit                      :" , nom_produit)
print("Type produit                        :" , nom_produit)
print(f"Référence                           :    {reference} ")
print("Poids                               :      " ,poids_kg, "kg")
print("Date de frabrication                :   " , date_fabrication )
print("Date limite de consommation         :   " ,date_limite )
print("Prix au kilo                        :       " , prix_kg, "€")
print("="*51)

cout_total = prix_kg * poids_kg

print(f"Prix total                          :        {cout_total:.2f} €")
print("="*51)
