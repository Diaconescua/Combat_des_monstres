from random import randint as r
from time import sleep as s


# Fonction pour lancer un dé (simulé par deux nombre aléatoire entre 1 et 6 qui sont addisionné)
def lancer_de():
  return r(1, 6) + r(1, 6)


# Initialisation des variables
niveau_vie = 20
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
nombre_combat = 0
combat_statut = "Il n'avait pas de dernier combat"
IsBoss = False
T = 0.5  #delay

while niveau_vie > 0:
  if IsBoss == False:
    force_adversaire = r(1, 7)
    print("\nVous tombez face à face avec un adversaire de difficulté :",
          force_adversaire)

    # Menu du jeu
    print("Que voulez-vous faire?")
    s(T)
    print("  1- Combattre cet adversaire")
    s(T)
    print("  2- Contourner cet adversaire et aller ouvrir une autre porte")
    s(T)
    print("  3- Afficher les règles du jeu")
    s(T)
    print("  4- Quitter la partie")
    s(T)
    choix = input("Entrez votre choix (1/2/3/4): ")

    if choix == '1':
      # Lancer le dé pour le combat
      score_de = lancer_de()

      nombre_combat += 1

      print("\nAdversaire :", nombre_combat)
      s(T)
      print("Force de l’adversaire :", force_adversaire)
      s(T)
      print("Niveau de vie de l’usager :", niveau_vie)
      s(T)
      print("Combat numéro ", nombre_combat, ":", nombre_victoires, "VS",
            nombre_defaites)
      s(T)
      print("Lancer du dé :", score_de)
      s(T)
      print("Dernier combat :", combat_statut)
      s(T)

      if score_de > force_adversaire:
        print("Vous avez remporté le combat!")
        niveau_vie += force_adversaire
        nombre_victoires_consecutives += 1
        nombre_victoires += 1
        combat_statut = "victoire"
        s(T)
        print("Niveau de vie:", niveau_vie)
        s(T)
        print("Nombre de victoires consécutives :",
              nombre_victoires_consecutives)
        s(T)
      else:
        print("Vous avez perdu le combat!")
        niveau_vie -= force_adversaire
        nombre_defaites += 1
        nombre_victoires_consecutives = 0
        combat_statut = "défaite"
        s(T)
        print("Niveau de vie:", niveau_vie)
        s(T)

    elif choix == '2':
      niveau_vie -= 1
      print("\nVous contournez l'adversaire et allez ouvrir une autre porte.")
      s(T)
      print("Niveau de vie de l’usager :", niveau_vie)
      s(T)

    elif choix == '3':
      print("Règles du jeu:")
      s(T)
      print(
          "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
      )
      s(T)
      print(
          "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire."
      )
      s(T)
      print(
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0."
      )
      s(T)
      print(
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie."
      )
      pass

    elif choix == '4':
      print("Merci et au revoir...")
      s(T)
      break

    if nombre_victoires_consecutives % 3 == 0:
      print("Vous avez atteint", nombre_victoires_consecutives,
            "victoires consécutives! Vous affrontez maintenant le boss!")
      s(T)
      force_adversaire = r(6, 10)
      IsBoss = True
      print("Boss de difficulté :", force_adversaire)
      s(T)

  # if boss == True
  else:
    print("\nVous tombez face à face avec un adversaire de difficulté :",
          force_adversaire)

    # Menu du jeu
    print("Que voulez-vous faire?")
    s(T)
    print("  1- Combattre cet adversaire")
    s(T)
    print("  2- Afficher les règles du jeu")
    s(T)
    print("  3- Quitter la partie")
    s(T)
    choix = input("Entrez votre choix (1/2/3): ")

    if choix == '1':
      # Lancer le dé pour le combat
      score_de = lancer_de()

      nombre_combat += 1

      print("\nAdversaire :", nombre_combat)
      s(T)
      print("Force de l’adversaire :", force_adversaire)
      s(T)
      print("Niveau de vie de l’usager :", niveau_vie)
      s(T)
      print("Combat numéro ", nombre_combat, ":", nombre_victoires, "VS",
            nombre_defaites)
      s(T)
      print("Lancer du dé :", score_de)
      s(T)
      print("Dernier combat :", combat_statut)
      s(T)

      if score_de > force_adversaire:
        print("Vous avez remporté le combat!")
        niveau_vie += force_adversaire
        nombre_victoires_consecutives += 1
        nombre_victoires += 1
        combat_statut = "victoire"
        IsBoss = False
        s(T)
        print("Niveau de vie:", niveau_vie)
        s(T)
        print("Nombre de victoires consécutives :",
              nombre_victoires_consecutives)
        s(T)
      else:
        print("Vous avez perdu le combat!")
        niveau_vie -= force_adversaire
        nombre_defaites += 1
        nombre_victoires_consecutives = 0
        combat_statut = "défaite"
        IsBoss = True
        s(T)
        print("Niveau de vie:", niveau_vie)
        s(T)

    elif choix == '2':
      print("Règles du jeu:")
      s(T)
      print(
          "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
      )
      s(T)
      print(
          "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire."
      )
      s(T)
      print(
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0."
      )
      s(T)
      print(
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie."
      )

    elif choix == '3':
      print("Merci et au revoir...")
      s(T)
      break

print("La partie est terminée, vous avez vaincu", nombre_victoires,
      "monstre(s).")
