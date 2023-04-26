
'''
Célèbre jeu du Chifoumi  
Choisis la pierre, la feuille ou les ciseaux,
ton adversaire fait de même,
La Pierre écrase les Ciseaux,
Les Ciseaux coupent la Feuille,
La Feuille recouvre la Pierre.
Le premier joueur à 3 points remporte la partie
'''

#variable pour recommencer le jeu
retry = "o"

while retry == "o" :
  
  from art import *
  print("\n")
  tprint("Jeu du Chifoumi")
  print("\n")
  print("le premier à 3 victoires gagne.")
  print("Enjoy !")
  print("\n")

  ptsJoueur=0
  ptsAdv=0

#le joueur entre son nom et celui de son adversaire 
  joueur=input("Entres ton nom : ")
  adv=input("Entres le nom de ton adversaire : ")
  print("\n")

#partie en 3 points
  while ptsJoueur<3 and ptsAdv<3 :


    #choix du joueur
      choix = input('Choisis entre "p" pour pierre, "f" pour feuille ou "c" pour ciseaux : ')

    #choix aléatoire de l'adversaire 
      seq=["p","f","c"]
      import random
      choixAdv=random.choice(seq)
  
    #affichage choix adversaire
      if choixAdv=="p":
        print(f"{adv} joue la Pierre")
      elif choixAdv=="f":
        print(f"{adv} joue la Feuille")
      else:
        print(f"{adv} joue les Ciseaux")

    #si le joueur choisit "p"
      if choix=="p" :
        if choixAdv=="p" :
          print("Match nul")
        elif choixAdv=="f" :
          print(f"La feuille enveloppe la pierre. {adv} remporte cette manche ! ")
          ptsAdv=ptsAdv+1 #l'adversaire gagne 1pt
        else :
          print(f"La pierre casse les ciseaux. Bravo {joueur} ! Tu remportes cette manche. ")
          ptsJoueur=ptsJoueur+1 #le joueur gagne 1pt

    #si le joueur choisit "f"
      elif choix=="f" :
        if choixAdv=="p" :
          print(f"La feuille enveloppe la pierre. Bravo {joueur} ! Tu remportes cette manche. ")
          ptsJoueur=ptsJoueur+1 #le joueur gagne 1pt
        elif choixAdv=="f" :
          print("Match nul")
        else :
          print(f"Les ciseaux coupent la feuille. {adv} remporte cette manche ! ")
          ptsAdv=ptsAdv+1 #l'adversaire gagne 1pt

    #si le joueur choisit "c"
      elif choix=="c" :
        if choixAdv=="p" :
          print(f"La pierre casse les ciseaux. {adv} remporte cette manche ! ")
          ptsAdv=ptsAdv+1 #l'adversaire gagne 1pt
        elif choixAdv=="f" :
          print(f"Les ciseaux coupent la feuille. Bravo {joueur} ! Tu remportes cette manche. ")
          ptsJoueur=ptsJoueur+1 #le joueur gagne 1pt
        else :
          print("Match nul")

    #le joueur essaye de tricher en faisant un choix non prévu 
      else :
        print(f"Tricheur ! '{choix}' n'est pas un choix valide. Tu perds un point. ")
        ptsJoueur=ptsJoueur-1 #le joueur perd 1pt

    #affichage du score
      print (f"{joueur} : {ptsJoueur} points ")
      print (f"{adv} : {ptsAdv} points ")
      print("\n")

#fin du jeu : victoire/défaite 
  if ptsJoueur == 3 :
    print(f"Bravo {joueur} ! Tu as gagné ! ")
  else :
    print(f"Looser ! Tu as perdu. Retentes ta chance. ;) ")
    print("\n")

  retry=input("On recommence ? (o/n) : ")
print(" ")

while ( retry != "o" and retry != "n" ) :
  retry = input("Oops.. On recommence ? (o/n) : ")

if retry=="n" :
  print ("")
  print ("Ok, merci d'avoir joué. A+ ")
           
