from DAO_produit import *
# la responsabilité de ce module est d'affiche la fiche d'un produit P



prix_produit = poids_kg * prix_kilo

print(f" Prix du produit        : {prix_produit:.2f} €")

print("="*20)
print("   Fiche produit ")
print("="*20)
print("Nom du produit           :", nom_produit)
print("Type du produit          :", type_produit)
print("Reference du produit     :", reference)
print("Poids                    :", poids_kg, "kg")
print("Date fabrication         :", date_fabrication)
print("Date limite consommation :", date_limite_consommation)
print(f"Prix au kilo             : {prix_kilo:.2f} €")
print(f"Prix du produit          : {prix_produit:.2f} €")





