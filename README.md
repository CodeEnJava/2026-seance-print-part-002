# 2026-seance-print-part-002
# 🐍 Mini-projet – Fiche produit

## Manipulation des variables, opérateurs, chaînes de caractères et `print()`

---

## 🎯 Objectif

Dans ce mini-projet, vous allez réaliser un programme Python permettant d'afficher la **fiche d'un produit**.

L'objectif est de réinvestir les notions étudiées dans les séances précédentes :

* création et utilisation de variables ;
* chaînes de caractères ;
* nombres entiers et décimaux ;
* opérations arithmétiques ;
* conversion de valeurs ;
* concaténation ;
* utilisation de `print()` ;
* affichage de plusieurs valeurs avec `print()` ;
* formatage simple des nombres avec `:.2f`.

> 💡 **Important :** le projet doit être réalisé uniquement avec les notions étudiées jusqu'à présent.
> Aucune fonction personnelle, boucle ou structure conditionnelle `if` n'est nécessaire.

---

# 📥 1. Préparer le projet dans PyCharm

Avant de commencer le projet, vous devez préparer votre environnement de travail.

### Étape 1 – Cloner le dépôt

Commencez par **cloner le dépôt GitHub** du projet sur votre ordinateur.

> ⚠️ **N'oubliez pas de cloner le dépôt avant de commencer votre travail.**

Une fois le dépôt cloné, ouvrez-le dans **PyCharm**.

### Étape 2 – Créer votre dossier personnel

Dans PyCharm, créez à la racine du projet un dossier portant **votre pseudo**.

Par exemple, si votre pseudo est :

```text
toto
```

vous devez créer :

```text
toto
```

### Étape 3 – Ajouter le module Python

À l'intérieur de votre dossier personnel, créez le module :

```text
fiche_produit.py
```

L'organisation de votre projet doit donc être similaire à :

```text
projet-fiche-produit/
│
├── README.md
│
├── toto/
│   └── fiche_produit.py
│
├── dupont/
│   └── fiche_produit.py
│
└── ...
```

Chaque stagiaire travaille **uniquement dans son propre dossier**.

> 💡 **Conseil :** vérifiez bien le nom de votre dossier et du fichier Python avant de commencer.

---

# 📦 2. Principe du projet

Le programme doit permettre d'afficher les informations concernant un produit.

Les informations à gérer sont :

| Information                 | Exemple       |
| --------------------------- | ------------- |
| Nom du produit              | Pommes Golden |
| Type de produit             | Fruit         |
| Référence                   | FR-POM-001    |
| Poids                       | 750 g         |
| Date de fabrication         | 2026-10-05    |
| Date limite de consommation | 2026-10-12    |
| Prix au kilo                | 2.49 €        |

Le programme devra transformer certaines informations avant leur affichage.

---

# 🧱 3. Créer les variables

Créer les variables suivantes :

```python
nom_produit = "Pommes Golden"
type_produit = "Fruit"
reference = "FR-POM-001"

poids_grammes = 750

date_fabrication = "2026-10-05"
date_limite_consommation = "2026-10-12"

prix_kilo = 2.49
```

### Questions

Pour chaque variable, déterminer son type :

```python
print(type(nom_produit))
print(type(type_produit))
print(type(reference))
print(type(poids_grammes))
print(type(date_fabrication))
print(type(date_limite_consommation))
print(type(prix_kilo))
```

À identifier :

* `str`
* `int`
* `float`

---

# ⚖️ 4. Convertir le poids

Le poids est enregistré dans la variable :

```python
poids_grammes = 750
```

Le programme doit afficher le poids en **kilogrammes**.

Rappel :

```text
1 kg = 1000 g
```

Créer une nouvelle variable :

```python
poids_kg
```

et effectuer le calcul nécessaire.

Pour 750 grammes, le résultat attendu est :

```text
0.75 kg
```

### À réaliser

```python
poids_kg = ...
```

Puis afficher :

```text
Poids : 0.75 kg
```

### Question

Quelle opération mathématique faut-il utiliser pour convertir des grammes en kilogrammes ?

---

# 💰 5. Afficher le prix

Le prix au kilo est stocké dans :

```python
prix_kilo = 2.49
```

Le prix doit être affiché avec **deux chiffres après la virgule**.

Le résultat attendu est :

```text
Prix au kilo : 2.49 €
```

Utiliser le formatage :

```python
:.2f
```

Exemple :

```python
print(f"Prix au kilo : {prix_kilo:.2f} €")
```

> 💡 Cette écriture permet d'afficher un nombre décimal avec exactement deux chiffres après la virgule.

---

# 🖨️ 6. Afficher les informations

Afficher maintenant les informations du produit avec `print()`.

Le résultat attendu doit être proche de :

```text
Nom du produit : Pommes Golden
Type de produit : Fruit
Référence : FR-POM-001
Poids : 0.75 kg
Date de fabrication : 2026-10-05
Date limite de consommation : 2026-10-12
Prix au kilo : 2.49 €
```

Chaque information doit être affichée sur une ligne.

---

# 🧩 7. Construire une fiche produit

Améliorer maintenant l'affichage.

Le programme doit produire :

```text
========================================
             FICHE PRODUIT
========================================

Nom du produit              : Pommes Golden
Type de produit             : Fruit
Référence                   : FR-POM-001
Poids                       : 0.75 kg
Date de fabrication         : 2026-10-05
Date limite de consommation : 2026-10-12
Prix au kilo                : 2.49 €

========================================
```

### Contraintes

L'affichage doit être réalisé avec `print()`.

Vous pouvez utiliser :

```python
print("========================================")
```

et plusieurs arguments :

```python
print("Nom du produit :", nom_produit)
```

---

# 🔢 8. Réinvestir les opérateurs

Le programme doit également effectuer des calculs.

À partir de :

```python
poids_grammes = 750
prix_kilo = 2.49
```

calculer le **prix correspondant au produit**.

### Rappel

Le prix est exprimé au kilogramme.

Le produit pèse :

```text
750 g = 0.75 kg
```

Il faut donc calculer :

```text
prix du produit = poids en kg × prix au kilo
```

Créer une variable :

```python
prix_produit
```

Pour notre exemple :

```text
0.75 × 2.49 = 1.8675
```

Le prix devra être affiché avec deux décimales :

```text
Prix du produit : 1.87 €
```

---

# 🧪 9. Tester avec un autre produit

Modifier les variables afin de créer une nouvelle fiche produit.

Utiliser par exemple :

```python
nom_produit = "Yaourt nature"
type_produit = "Produit laitier"
reference = "PL-YAO-025"

poids_grammes = 125

date_fabrication = "2026-10-06"
date_limite_consommation = "2026-10-20"

prix_kilo = 3.20
```

Le programme doit automatiquement recalculer :

* le poids en kilogrammes ;
* le prix du produit ;
* l'affichage des informations.

### Résultat attendu

Le poids doit être :

```text
0.125 kg
```

Le prix du produit doit être calculé à partir du poids et du prix au kilo.

> 💡 Lors de l'affichage, le poids pourra être présenté avec deux décimales :
>
> ```text
> Poids : 0.13 kg
> ```

---

# ⭐ 10. Challenge – Utiliser `sep`

Modifier l'affichage de la référence afin d'obtenir :

```text
Référence : PL-YAO-025
```

Puis expérimenter avec `sep` :

```python
print("PL", "YAO", "025", sep="-")
```

Observer le résultat.

### Question

Quel est le rôle du paramètre `sep` dans `print()` ?

---

# ⭐ 11. Challenge – Utiliser `end`

Expérimenter avec :

```python
print("Nom du produit :", end=" ")
print(nom_produit)
```

Observer le résultat.

Puis expliquer la différence avec :

```python
print("Nom du produit :")
print(nom_produit)
```

### Question

Quel est le rôle du paramètre `end` dans `print()` ?

---

# 🧠 12. Questions de synthèse

Répondre aux questions suivantes.

### Question 1

Quel est le type de la variable :

```python
poids_grammes = 750
```

### Question 2

Quel est le type de :

```python
prix_kilo = 2.49
```

### Question 3

Pourquoi la variable :

```python
reference = "FR-POM-001"
```

est-elle une chaîne de caractères et non un nombre ?

### Question 4

Quelle opération permet de convertir les grammes en kilogrammes ?

### Question 5

Quelle est la différence entre :

```python
+
```

utilisé avec des nombres et :

```python
+
```

utilisé avec des chaînes de caractères ?

### Question 6

À quoi sert :

```python
:.2f
```

### Question 7

À quoi sert le paramètre :

```python
sep
```

dans `print()` ?

### Question 8

À quoi sert le paramètre :

```python
end
```

dans `print()` ?

---

# 📦 13. Livrable

Votre dossier personnel doit contenir au minimum :

```text
votre-pseudo/
│
└── fiche_produit.py
```

Le programme doit permettre de modifier facilement les informations du produit :

```python
nom_produit = "..."
type_produit = "..."
reference = "..."

poids_grammes = ...

date_fabrication = "..."
date_limite_consommation = "..."

prix_kilo = ...
```

et de générer automatiquement la fiche correspondante.

### 📤 Avant de terminer

Vérifiez que :

* votre dossier porte bien votre pseudo ;
* le fichier s'appelle bien `NAFAA-yassine/fiche_produit.py` ;
* votre programme fonctionne sans erreur ;
* les calculs sont corrects ;
* l'affichage correspond aux consignes ;
* vous avez enregistré votre travail ;
* votre fichier est bien placé dans votre dossier personnel.

---

# 🎯 Compétences mobilisées

À l'issue du mini-projet, vous devez être capable de :

* créer et utiliser des variables ;
* identifier les principaux types de données ;
* manipuler des chaînes de caractères ;
* effectuer des calculs avec des nombres ;
* utiliser les opérateurs arithmétiques ;
* convertir une unité à l'aide d'un calcul ;
* utiliser `print()` pour afficher des informations ;
* afficher plusieurs éléments avec `print()` ;
* utiliser `sep` ;
* utiliser `end` ;
* afficher un nombre avec deux décimales ;
* construire un programme simple à partir de plusieurs variables.

---

# 🚀 Pour aller plus loin

Dans une prochaine séance, le programme pourra être amélioré pour :

* demander les informations du produit à l'utilisateur ;
* vérifier les données saisies ;
* calculer automatiquement d'autres informations ;
* utiliser des fonctions ;
* organiser le programme en plusieurs parties.
