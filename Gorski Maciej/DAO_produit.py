import produit_pomme, produit_yaourt, produit_cerise

# On peut imaginer que l'ensemble des produits provient d'une
# base de données
# produits ==> peut être considéré comme une table
produits = [produit_pomme.dict_produit_pomme,
            produit_yaourt.dict_produit_yaourt,
            produit_cerise.dict_produit_cerise]

# choix du produit
# 0 pomme
# 1 yaourt
# 2 cerise

produit = produits[2]


nom_produit =produit[ "nom_produit"]
type_produit = produit[ "type_produit"]
reference = produit[ "reference"]

poids_grammes = produit[ "poids_grammes"]
poids_kg = produit[ "poids_kg"]


date_fabrication = produit[ "date_fabrication"]
date_limite_consommation = produit[ "date_limite_consommation"]

prix_kilo =  produit[ "prix_kilo"]