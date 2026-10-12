# La responsabilité de ce module:
# regrouper l'ensemble des informations sur le produit pomme,
# et chaque information est composée d'une clé et d'une valeur.
# Mise en place d'un dictionnaire

poids_grammes = 750

# On peut imaginer que ce dictionnaire est un ligne de données qui se trouve
# dans la table produits

dict_produit_pomme = {
    "nom_produit" : "Pommes Golden",
    "type_produit" : "Fruit",
    "reference" : "FR-POM-001",
    "poids_grammes" : poids_grammes,
    "poids_kg" : (poids_grammes / 1000),
    "date_fabrication" : "2026-10-05",
    "date_limite_consommation" : "2026-10-12",
    "prix_kilo" : 2.49

}




