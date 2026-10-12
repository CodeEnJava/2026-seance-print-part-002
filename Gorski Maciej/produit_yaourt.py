# La responsabilité de ce module:
# regrouper l'ensemble des informations sur le produit Yaourt nature,
# et chaque information est composée d'une clé et d'une valeur.
# Mise en place d'un dictionnaire

poids_grammes = 125

dict_produit_yaourt = {
    "nom_produit" : "Yaourt nature",
    "type_produit" : "Produit laitier",
    "reference" : "PL-YAO-025",
    "poids_grammes" : poids_grammes,
    "poids_kg" : (poids_grammes / 1000),
    "date_fabrication" : "2026-10-06",
    "date_limite_consommation" : "2026-10-20",
    "prix_kilo" : 3.20

}