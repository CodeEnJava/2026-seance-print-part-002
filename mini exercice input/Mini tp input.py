from platform import freedesktop_os_release
#TP1
user_name= str(input("entrer votre nom : "))
user_name = user_name.capitalize()
print(f"Bienvenue a toi honorable {user_name} ")


#TP2

prenom = str(input("entrer votre prénom : "))
nom    = str(input("entrer votre nom : "))

pseudo = prenom [0:3] + nom [0:3]

print(f"Ton Nouveau nom sera {pseudo}")

#tp3

a = int(input("entrer un un nombre entier : "))
b = int(input("entrer un deuxieme nombre entier : "))



