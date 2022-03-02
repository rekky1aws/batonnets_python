import random

def affichage(nb_batons): #Fonction permettant d'afficher le nombre de batons (nb_batons) donné.
	for i in range(3): #Trois lignes
		for j in range(nb_batons): #Nombre de batons
			print("|", end="")
			if j != (nb_batons-1): #On a les 3 espaces entre chaque batons, sauf si on vient de print le dernier baton
				print("   ", end="")
		print()

def menu_difficulty(): #Affichage du menu des différentes difficultées
	print("\n-- Mode de jeu --")
	print("\t0 - Novice (L'ordinateur jouera toujours 1)")
	print("\t1 - Facile") #Ordi joue au pif entre 1 et 3
	print("\t2 - Difficile") #Ordi joue au pif entre 1 et 3 sauf dernier tour ou il laisse qu'un seul baton s'il peut
	print("\t3 - Multijoueur") #Les joueurs jouent chacun leur tour
	#NON IMPLÉMENTÉ ! #print("\t4 - Impossible") #Mode caché : Impossible, l'Ordi optimise tous ses coups

def player1():
	number=-1
	while number<0 or number>3:
		print("Combien de batonnets prenez vous (1,2,3) : ", end="")
		number=input()
		if number.isnumeric():
			number=int(number)
		else:
			number=-1
	return number


def player2(batons_restants, difficulty):
	if batons_restants==1: #S'il ne reste plus qu'une seul baton, cela ne sert pas de demander
		return 1

	if difficulty==0: #Novice
		return 1

	elif difficulty==1: #Facile
		return random.randint(1,3)

	elif difficulty==2: #Moyen
		if batons_restants>4:
			return random.randint(1,3)
		else:
			return batons_restants-1

	elif difficulty==3: #Multijoueur
		return player1()

#Selection Mode de Jeu
gamemode=-1
while gamemode<0 or gamemode>3: #changer la limite haute à 4 si implementation mode Impossible
	menu_difficulty()
	print("Veuillez saisir le mode de jeu : ", end="")
	gamemode=input()
	if gamemode.isnumeric():
		gamemode=int(gamemode)
	else:
		gamemode=-1

#Paramètres initiaux
batons=13+random.randint(0,2) #Aléatoire sur le nombre batons

player1_first=random.randint(0,1) #Pile ou face pour déterminer l'ordre de jeu

last_player=-1

#Gameplay

#Joueur 1 = Joueur
#Joueur 2 = Ordinateur (ou Joueur si gamemode==3)
if (batons%4==1 and gamemode==4) or player1_first==0: #Le cas ou le joueur 1 joue en premier
	while batons>0: 
		affichage(batons)
		print("Joueur A :")
		batons-=player1()
		last_player=1
		if batons>0: #on vérifie si la partie n'est pas déja finie
			affichage(batons)
			print("Joueur B :")
			batons-=player2(batons, gamemode)
			last_player=2
else: #Le cas ou le joueur 1 joue en second
	while batons>0:
		affichage(batons)
		print("Joueur A :")
		batons-=player2(batons, gamemode)
		last_player=1
		if batons>0:
			affichage(batons)
			print("Joueur B :")
			batons-=player1()
			last_player=2

#print(player2(batons, gamemode))
if last_player==1:
	print("\n\nLe joueur B a gagné !")
elif last_player==2:
	print("\n\nLe joueur A a gagné !")
else:
	print("\n\n ## ERREUR ## \n\tJoueur Gagnant non determiné")





print("Fin") #DEBUG

