from random import randint as r
from time import sleep as s


# Fonction pour lancer un dé (simulé par deux nombre aléatoire entre 1 et 6 qui sont addisionné)
def lancer_de():
  return r(1, 6) + r(1, 6)


# Initialisation des variables
niveau_vie = 20
adversaire = 'adversaire'
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
nombre_combat = 0
force_adversaire = r(1, 7)
combat_statut = "Il n'avait pas de dernier combat"
IsBoss = False
T = 0.5  #delay

# la boucle qui fait jouer le jeux a l'infinie juusqu'a ce que la joueur veux plus.
while niveau_vie > 0:
  if (IsBoss == False and combat_statut != "Il n'avait pas de dernier combat" and (choix == '1' or choix == '2')):
      force_adversaire = r(1, 7)
      adversaire = 'adversaire'
  else:
    adversaire = 'boss'
  print("\nVous tombez face à face avec un adversaire de difficulté :",
        force_adversaire)

  # je donne 4 option au joueur(combattre les enemies, contourner les enemies, montrer les regles et quitter le jeux)
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

  # le joueur lance le dé, le joueur voit le numero et le niveau de l'adversaire, aussi, son niveau de vie, numero de combat et le status du dernier combat
  if choix == '1':
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

    # si le dé est plus fort que l'enemie le joueur a gagne le combat et il voit son nombre de vie et nombre de victoires consécutives
    # il perd le meme nombre de vie que le nombre de vie que son enemie, il a une victoire consecutive de plus et une victoire de plus
    if score_de > force_adversaire:
      print("Vous avez remporté le combat!")
      niveau_vie += force_adversaire
      nombre_victoires_consecutives += 1
      nombre_victoires += 1
      combat_statut = "victoire"
      if IsBoss == True:
        IsBoss = False
      s(T)
      print("Niveau de vie:", niveau_vie)
      s(T)
      print("Nombre de victoires consécutives :",
            nombre_victoires_consecutives)
      s(T)
    # si l'enemie est plus fort que le dé le joueur perd
    # il perd le meme nombre de vie que le nombre de vie que son enemie, il a 0 victoire consecutive et defaite de plus
    else:
      print("Vous avez perdu le combat!")
      niveau_vie -= force_adversaire
      nombre_defaites += 1
      nombre_victoires_consecutives = 0
      combat_statut = "défaite"
      s(T)
      print("Niveau de vie:", niveau_vie)
      s(T)
  # le joueur va voir une autre porte avec un autre enemie il voit son nombre de vie car il perd une vie
  elif choix == '2':
    niveau_vie -= 1
    if IsBoss == True:
      force_adversaire = r(6, 10)
    print("\nVous contournez l'adversaire et allez ouvrir une autre porte.")
    s(T)
    print("Niveau de vie de l’usager :", niveau_vie)
    s(T)
  # ca montre les regles du jeux
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


  elif choix == '4':
    print("Merci et au revoir...")
    s(T)
    break

  # si il a un nombre de victoirs consecutive divisible pars 3 il combat le boss avec un niveau plus elever que les enemies
  if  IsBoss == False and nombre_victoires_consecutives != 0 and nombre_victoires_consecutives % 3 == 0:
    print("Vous avez atteint", nombre_victoires_consecutives,
          "victoires consécutives! Vous affrontez maintenant le boss!")
    s(T)
    force_adversaire = r(6, 10)
    IsBoss = True
    print("Boss de difficulté :", force_adversaire)
    s(T)
