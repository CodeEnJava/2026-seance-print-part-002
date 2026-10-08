nom_produit = "Pommes Golden"
type_produit = "Fruit"
reference = "FR-POM-001"

poids_grammes = 750
poids_kg = poids_grammes / 1000


date_fabrication = "2026-10-05"
date_limite_consommation = "2026-10-12"

prix_kilo = 2.49

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





