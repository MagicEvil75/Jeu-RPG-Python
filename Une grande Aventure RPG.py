import random
import json
import os

global argent
argent = 0
global Vie
Vie = 20
global Première_Quête
Première_Quête = False
global Deuxième_Quête
Deuxième_Quête = False
global Troisième_Quête
Troisième_Quête = False
Quatrième_Quête_partie1 = False
global Quatrième_Quête
Quatrième_Quête = False
global Cinquième_Quête
Cinquième_Quête = False
global Sixième_Quête
Sixième_Quête = False
global Septième_Quête
Septième_Quête = False
global personnage_selectionne
personnage_selectionne = False
global emplacement_actuel
emplacement_actuel = ""
global Try_code
Try_code = False
global développeur
développeur = False
global sauvegarde_chargee
sauvegarde_chargee = False

chemin_fichier = "C:\\Users\\ethan\\OneDrive\\Documents\\sauvegarde_jeu_python.json"

# Répertoire des sauvegardes
dossier_sauvegardes = "sauvegardes"
os.makedirs(dossier_sauvegardes, exist_ok=True)

# Fonction pour le chemin fichier
def obtenir_chemin_fichier(nom_sauvegarde):
    return os.path.join(dossier_sauvegardes, f"{nom_sauvegarde}.json")

# Fonction pour sauvegarder l'état du jeu
def sauvegarder_jeu():
    global argent, Vie, Première_Quête, Deuxième_Quête, Troisième_Quête, Quatrième_Quête_partie1, Quatrième_Quête, Cinquième_Quête, Sixième_Quête, personnage, caractéristiques, Force, Magie, Intelligence, Adresse, dragon, personnage_selectionne, emplacement_actuel, développeur, sauvegarde_chargee
    
    if sauvegarde_chargee is True:
        nom_sauvegarde = nom_sauvegarde_chargée
        print(f"\nUne sauvegarde a été chargée. La partie sera sauvegardée sous le nom : {nom_sauvegarde}") 
        choix = input("Voulez-vous sauvegarder sous ce nom ? (oui/non) : ")
        if choix == 'oui':
            chemin_fichier = obtenir_chemin_fichier(nom_sauvegarde)
            with open(chemin_fichier, 'w') as fichier:    
                data = {
                    "argent": argent,
                    "Vie": Vie,
                    "Première_Quête": Première_Quête,
                    "Deuxième_Quête": Deuxième_Quête,
                    "Troisième_Quête": Troisième_Quête,
                    "Quatrième_Quête_partie1": Quatrième_Quête_partie1,
                    "Quatrième_Quête": Quatrième_Quête,
                    "Cinquième_Quête": Cinquième_Quête,
                    "Sixième_Quête": Sixième_Quête,
                    "personnage" : personnage,
                    "caractéristiques": caractéristiques,
                    "Force": Force,
                    "Magie": Magie,
                    "Intelligence": Intelligence,
                    "Adresse": Adresse,
                    "dragon": dragon,
                    "personnage_selectionne": personnage_selectionne,
                    "emplacement_actuel" : emplacement_actuel,
                    "développeur" : développeur
                }
                json.dump(data, fichier)
        elif choix == 'non':
            nom_sauvegarde = input("\nNommez votre sauvegarde (sans oublier de remplacer les espaces par _) : ")
            chemin_fichier = obtenir_chemin_fichier(nom_sauvegarde)
            with open(chemin_fichier, 'w') as fichier:    
                data = {
                    "argent": argent,
                    "Vie": Vie,
                    "Première_Quête": Première_Quête,
                    "Deuxième_Quête": Deuxième_Quête,
                    "Troisième_Quête": Troisième_Quête,
                    "Quatrième_Quête_partie1": Quatrième_Quête_partie1,
                    "Quatrième_Quête": Quatrième_Quête,
                    "Cinquième_Quête": Cinquième_Quête,
                    "Sixième_Quête": Sixième_Quête,
                    "personnage" : personnage,
                    "caractéristiques": caractéristiques,
                    "Force": Force,
                    "Magie": Magie,
                    "Intelligence": Intelligence,
                    "Adresse": Adresse,
                    "dragon": dragon,
                    "personnage_selectionne": personnage_selectionne,
                    "emplacement_actuel" : emplacement_actuel,
                    "développeur" : développeur
                }
                json.dump(data, fichier)
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.")
            sauvegarder_jeu()
    else:
        nom_sauvegarde = input("\nNommez votre sauvegarde (sans oublier de remplacer les espaces par _) : ")
        chemin_fichier = obtenir_chemin_fichier(nom_sauvegarde)
        with open(chemin_fichier, 'w') as fichier:    
            data = {
                "argent": argent,
                "Vie": Vie,
                "Première_Quête": Première_Quête,
                "Deuxième_Quête": Deuxième_Quête,
                "Troisième_Quête": Troisième_Quête,
                "Quatrième_Quête_partie1": Quatrième_Quête_partie1,
                "Quatrième_Quête": Quatrième_Quête,
                "Cinquième_Quête": Cinquième_Quête,
                "Sixième_Quête": Sixième_Quête,
                "personnage" : personnage,
                "caractéristiques": caractéristiques,
                "Force": Force,
                "Magie": Magie,
                "Intelligence": Intelligence,
                "Adresse": Adresse,
                "dragon": dragon,
                "personnage_selectionne": personnage_selectionne,
                "emplacement_actuel" : emplacement_actuel,
                "développeur" : développeur
            }
            json.dump(data, fichier)

    # Si la partie a été chargée à partir d'une sauvegarde, utilisez automatiquement le nom de cette sauvegarde
  
    print(f"\nLe jeu a été sauvegardé avec succès sous le nom : {nom_sauvegarde}")

# Fonction pour charger l'état du jeu
def charger_jeu(nom_sauvegarde):
    global argent, Vie, Première_Quête, Deuxième_Quête, Troisième_Quête, Quatrième_Quête_partie1, Quatrième_Quête, Cinquième_Quête, Sixième_Quête, personnage, caractéristiques, Force, Magie, Intelligence, Adresse, dragon, personnage_selectionne, emplacement_actuel, développeur
    
    chemin_fichier = obtenir_chemin_fichier(nom_sauvegarde)
    try:
        with open(chemin_fichier, "r") as fichier:
            data = json.load(fichier)
            argent = data["argent"]
            Vie = data["Vie"]
            Première_Quête = data["Première_Quête"]
            Deuxième_Quête = data["Deuxième_Quête"]
            Troisième_Quête = data["Troisième_Quête"]
            Quatrième_Quête_partie1 = data["Quatrième_Quête_partie1"]
            Quatrième_Quête = data["Quatrième_Quête"]
            Cinquième_Quête = data["Cinquième_Quête"]
            Sixième_Quête = data["Sixième_Quête"]
            personnage = data["personnage"]
            caractéristiques = data["caractéristiques"]
            Force = data["Force"]
            Magie = data["Magie"]
            Intelligence = data["Intelligence"]
            Adresse = data["Adresse"]
            dragon = data["dragon"]
            personnage_selectionne = data["personnage_selectionne"]
            emplacement_actuel = data["emplacement_actuel"]
            développeur = data["développeur"]
            print("Le jeu a été chargé avec succès.")
            personnage_incarné()
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée sous le nom :", nom_sauvegarde)
        print("Réessayez ou bien recommencez une nouvelle partie.")
        début_du_jeu()

# Fonction pour lister les sauvegardes disponibles
def lister_sauvegardes():
    sauvegardes = [f.split(".")[0] for f in os.listdir(dossier_sauvegardes) if f.endswith(".json")]
    return sauvegardes

# Gérer les sauvegardes
def gerer_les_sauvegardes():
    choix = input("Voulez-vous supprimer une sauvegarde ? (oui/non) : ")
    if choix.lower() == 'oui':
        sauvegardes = lister_sauvegardes()
        if sauvegardes:
            print("Sauvegardes disponibles :")
            for i, nom in enumerate(sauvegardes):
                print(f"{i + 1}. {nom}")
                choix_sauvegarde = int(input("Entrez le numéro de la sauvegarde à supprimer : ")) - 1
            if 0 <= choix_sauvegarde < len(sauvegardes):
                nom_sauvegarde = sauvegardes[choix_sauvegarde]
                supprimer_sauvegarde(nom_sauvegarde)
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                gerer_les_sauvegardes()
        else:
            print("Aucune sauvegarde disponible.")
            menu_principal()
    else:
        menu_principal()
        
# Fonction pour supprimer une sauvegarde
def supprimer_sauvegarde(nom_sauvegarde):
    chemin_fichier = obtenir_chemin_fichier(nom_sauvegarde)
    try:
        os.remove(chemin_fichier)
        print(f"Sauvegarde '{nom_sauvegarde}' supprimée avec succès.")
    except FileNotFoundError:
        print(f"Aucune sauvegarde trouvée sous le nom : {nom_sauvegarde}")

# Fonction pour vérifier la vie du joueur
def verifier_vie():
    global Vie
    if Vie <= 0:
        print("Vous êtes mort.")
        print("--- Que voulez-vous faire ? ---")
        print("1. Recommencer une partie.")
        print("2. Recharger une sauvegarde.")
        choix = input("Entrez le numéro de votre choix (1, 2 ou 3) : ")
        if choix == '1':
            choisir_personnage()
        elif choix == '2':
            sauvegardes = lister_sauvegardes()
            if sauvegardes:
                print("Sauvegardes disponibles :")
                for i, nom in enumerate(sauvegardes):
                    print(f"{i + 1}. {nom}")
                choix_sauvegarde = int(input("Entrez le numéro de la sauvegarde à charger : ")) - 1
                if 0 <= choix_sauvegarde < len(sauvegardes):
                    charger_jeu(sauvegardes[choix_sauvegarde])
                    reprendre_jeu()
                else:
                    print("Choix invalide. Démarrage d'une nouvelle partie.")
                    choisir_personnage()
            else:
                print("Aucune sauvegarde disponible. Démarrage d'une nouvelle partie.")
                choisir_personnage()
    else:
        reprendre_jeu()
    
    return Vie        

# Définir où reprendre le jeu
def reprendre_jeu():
    global emplacement_actuel
    if emplacement_actuel == 'Menu principal':
        menu_principal()
    elif emplacement_actuel == "Ravenwood":
        ravenwood()
    elif emplacement_actuel == "Tryndamere":
        tryndamere()
    elif emplacement_actuel == 'Mordor':
        mordor()
    
# Début du jeu : 1ère Etape, choisir le personnage
def choisir_personnage():
    global personnage_selectionne
    personnage_selectionne = False
    print("\nQuel personnage voulez-vous choisir ?")
    print("1. Magicien : Maîtrise la magie, possède des sorts spéciaux. Force : 6; Défense : 10; Intelligence : 18; Adresse : 10; Magie : 18; Vie : 20")
    print("2. Guerrier : Maîtrise la force, possède des armes. Force : 18; Défense : 16; Intelligence : 6; Adresse : 10; Magie : 4; Vie : 20")
    print("3. Archer : Maîtrise les armes longues portées, possède des armes. Force : 10; Intelligence : 14; Adresse : 18; Magie : 6; Vie : 20")
    print("4. Voleur : Maîtrise la discrétion, possède des armes. Force : 14; Intelligence : 10; Adresse : 18; Magie : 6; Vie : 20")
    print("5. Assassin : Maîtrise la discrétion et l'art de tuer, possède des armes. Force : 18; Intelligence : 14; Adresse : 10; Magie : 6; Vie : 20")
    choix = input("Entrez le numéro du personnage que vous voulez choisir (entre 1 et 5) : ")
    global dragon
    dragon = False
    global développeur
    développeur = False

    if choix == '1':
        global personnage
        personnage = "Magicien"
        global caractéristiques
        caractéristiques = "Maîtrise la magie, possède des sorts spéciaux"
        global Force
        Force = 6
        global Défense
        Défense = 10
        global Intelligence
        Intelligence = 18
        global Adresse
        Adresse = 10
        global Magie
        Magie = 18
    elif choix == '2':
        personnage = "Guerrier"
        caractéristiques = "Maîtrise la force, possède des armes"
        Force = 18
        Défense = 16
        Intelligence = 6
        Adresse = 10
        Magie = 4
    elif choix == '3':
        personnage = "Archer"
        caractéristiques = "Maîtrise les armes longues portées, possède des armes"
        Force = 10
        Défense = 14
        Intelligence = 14
        Adresse = 18
        Magie = 6
    elif choix == '4':
        personnage = "Voleur"
        caractéristiques = "Maîtrise la discrétion, possède des armes"
        Force = 14
        Défense = 20
        Intelligence = 10
        Adresse = 18
        Magie = 6
    elif choix == '5':
        personnage = "Assassin"
        caractéristiques = "Maîtrise la discrétion et l'art de tuer, possède des armes"
        Force = 18
        Défense = 8
        Intelligence = 14
        Adresse = 10
        Magie = 6
    elif choix.lower() == 'dragon':
        personnage = "Dragon"
        caractéristiques = "Maîtrise la magie, possède des sorts spéciaux"
        Force = 20
        Défense = 20
        Intelligence = 20
        Adresse = 20
        Magie = 20
        dragon = True
    elif choix.lower() == 'développeur':
        personnage = "Dragon"
        caractéristiques = "Maîtrise la magie, possède des sorts spéciaux"
        Force = 20
        Défense = 20
        Intelligence = 20
        Adresse = 20
        Magie = 20
        dragon = True
        développeur = True
    else:
        print("Choix invalide. Veuillez sélectionner un numéro entre 1 et 5.")
        return choisir_personnage()

    personnage_selectionne = True
    personnage_incarné()
    return personnage, Force, Intelligence, Adresse, Magie, Vie, dragon

# Changer de personnage
def changer_personnage():
    global personnage_selectionne
    personnage_selectionne = False
    global argent
    global développeur
    print("\nEn quel personnage voulez-vous vous transformer ?")
    print("1. Magicien : Maîtrise la magie, possède des sorts spéciaux. Force : 6; Intelligence : 18; Adresse : 10; Magie : 20; Vie : 20")
    print("2. Guerrier : Maîtrise la force, possède des armes. Force : 20; Intelligence : 6; Adresse : 10; Magie : 4; Vie : 20")
    print("3. Archer : Maîtrise les armes longues portées, possède des armes. Force : 10; Intelligence : 14; Adresse : 20; Magie : 6; Vie : 20")
    print("4. Voleur : Maîtrise la discrétion, possède des armes. Force : 14; Intelligence : 10; Adresse : 20; Magie : 6; Vie : 20")
    print("5. Assassin : Maîtrise la discrétion et l'art de tuer, possède des armes. Force : 20; Intelligence : 6; Adresse : 10; Magie : 6; Vie : 20")
    choix = input("Entrez le numéro du personnage que vous voulez choisir (entre 1 et 5) : ")
    if choix == '1':
        global personnage
        personnage = "Magicien"
        global caractéristiques
        caractéristiques = "Maîtrise la magie, possède des sorts spéciaux"
        global Force
        Force = 6
        global Défense
        Défense = 12
        global Intelligence
        Intelligence = 18
        global Adresse
        Adresse = 10
        global Magie
        Magie = 20
        magasin_potions()
    elif choix == '2':
        personnage = "Guerrier"
        caractéristiques = "Maîtrise la force, possède des armes"
        Force = 20
        Défense = 16
        Intelligence = 6
        Adresse = 10
        Magie = 4
        magasin_potions()
    elif choix == '3':
        personnage = "Archer"
        caractéristiques = "Maîtrise les armes longues portées, possède des armes"
        Force = 10
        Défense = 14
        Intelligence = 14
        Adresse = 20
        Magie = 6
        magasin_potions()
    elif choix == '4':
        personnage = "Voleur"
        caractéristiques = "Maîtrise la discrétion, possède des armes"
        Force = 14
        Défense = 20
        Intelligence = 10
        Adresse = 20
        Magie = 6
        magasin_potions()
    elif choix == '5':
        personnage = "Assassin"
        caractéristiques = "Maîtrise la discrétion et l'art de tuer, possède des armes"
        Force = 20
        Défense = 12
        Intelligence = 6
        Adresse = 10
        Magie = 6
        magasin_potions()
    elif choix.lower() == 'développeur':
        argent = random.randint(300, 600)
        choisir_personnage()
    else:
        print("Choix invalide. Veuillez sélectionner un numéro entre 1 et 5.")
        return changer_personnage()

    personnage_selectionne = True
    personnage_incarné()
    return personnage, Force, Intelligence, Adresse, Magie, Vie, dragon

#Fonction du magasin
def magasin():
    global Try_code
    print("\nBienvenue dans le magasin !\n")
    print("Vous pouvez acheter des objets pour augmenter vos statistiques.")
    print("1. Armes et armures.")
    print("2. Objets et potions")
    print("3. Quitter le magasin")
    choix = input("Entrez le numéro de votre choix (1, 2 ou 3) : ")
    if choix == '1':
        magasin_armes()
    elif choix == '2':
        magasin_potions()
    elif choix == '3':
        print("Merci d'avoir visité le magasin !")
        menu_principal()
    elif choix.lower() == 'testeur_jeu':
        if Try_code is False:
            Try_code = True
            global argent
            argent += 5000
            print("Tu gagnes 5000 pièces d'or.")
            magasin()
        else:
            print("Tu as déjà utilisé le code.")
            magasin()
    else: 
        print("Choix invalide. Veuillez sélectionner une option valide.")
        magasin()
    
# Fonction pour les armes et armures
def magasin_armes():
    global argent
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global Vie
    global personnage
    global caractéristiques
    print(f"\nVous avez actuellement {argent} pièces d'or.")
    print("Voici les armes et armures disponibles :")
    print("1. Epee de guerre : + 5 de force (50 pièce d'or).")
    print("2. Bouclier : + 2 de défense (20 pièces d'or).")
    print("3. Arc : + 2 d'adresse (30 pièces d'or).")
    print("4. Couteau : + 1 de force (10 pièces d'or).")
    print("5. Armure de métal : + 7 de défense (65 pièces d'or).")
    print("6. Baguette magique : + 10 de magie (200 pièces d'or).")
    print("7. Talisman magique : + 6 de magie, vie au maximum + bonus de 10 points de vie (300 pièces d'or).")
    print("10. Revenir à l'accueil du magasin")
    choix_arme = input("Entrez le numéro de l'arme que vous souhaitez recevoir (entre 1 et 7) ou 10 si vous voulez revenir à l'accueil du magasin : ")
    if choix_arme == '1':
        if argent >= 50:
            print("\nVous avez acheté l'épée de guerre.")
            Force += 5
            argent -= 50
            if Force >= 20: 
                Force = 20
                magasin_armes()
            else:
                print("\nVous n'avez pas assez d'argent pour acheter cette arme.")
                magasin_armes()
    elif choix_arme == '2':
        if argent >= 20:
            print("\nVous avez acheté le bouclier.")
            Défense += 2
            argent -= 20
            if Défense >= 20: 
                Défense = 2
            magasin_armes()
        else:
            print("\nVous n'avez pas assez d'argent pour acheter ce bouclier.")
            magasin_armes()
    elif choix_arme == '3':
        if argent >= 30:
            print("\nVous avez acheté l'arc.")
            Adresse += 2
            argent -= 30
            if Adresse >= 20: 
                Adresse = 20
            magasin_armes()
        else:
            print("\nVous n'avez pas assez d'argent pour acheter cet arc.")
            magasin_armes()
    elif choix_arme == '4':
        if argent >= 10:
            print("\nVous avez acheté le couteau.")
            Force += 1
            argent -= 10
            if Force >= 20: 
                Force = 20
            magasin_armes()
        else:
            print("\nVous n'avez pas assez d'argent pour acheter ce couteau.")
            magasin_armes()
    elif choix_arme == '5':
        if argent >= 65:
            print("\nVous avez acheté l'armure de métal.")
            Défense += 7
            argent -= 65
            if Défense >= 20: 
                Défense = 20
            magasin_armes()
        else:
            print("\nVous n'avez pas assez d'argent pour acheter cette armure.")
            magasin_armes()
    elif choix_arme == '6':
        if argent >= 200:
            print("\nVous avez acheté la baguette magique.")
            Magie += 10
            argent -= 200
            if Magie >= 20:
                Magie = 20
            magasin_armes()
    elif choix_arme == '7':
        if argent >= 300:
            print("Vous avez acheté le talisman magique.")
            Magie += 10
            Vie = 20
            Vie += 10
            argent -= 300
            if Magie >= 20:
                Magie = 20
            magasin_armes()
    elif choix_arme == '10':
        magasin()
    else:
        print("\nChoix invalide. Veuillez sélectionner un numéro entre 1 et 6.")
        magasin_armes()

# Fonction pour les objets et les potions
def magasin_potions():
    global argent
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global Vie
    global personnage
    global caractéristiques
    global dragon
    print(f"\nVous avez actuellement {argent} pièces d'or.")
    print("Voici les objets disponibles :")
    print("1. Potion de force (10 points de force) - 250 pièces d'or")
    print("2. Potion de magie (10 points de magie) - 250 pièces d'or")
    print("3. Potion de vie (10 points de vie) - 50 pièces d'or")
    print("4. Potion de transformation (Change de personnage) - 300 pièces d'or")
    print("5. Potion de transformation en dragon (Toutes les capacités au maximum + transformation en dragon) - 1000 pièces d'or")
    print("6. Revenir à l'accueil du magasin")
    choix_objet = input("Entrez le numéro de l'objet que vous souhaitez acheter (entre 1 et 4) ou 5 si vous voulez revenir à l'accueil du magasin : ")
    if choix_objet == '1':
        if argent >= 250:
            print("\nVous avez acheté une potion de force.")
            Force += 10
            argent -= 250
            if Force >= 20: 
                Force = 20
            magasin_potions()
        else:
            print("\nVous n'avez pas assez d'argent pour acheter cette potion.")
            magasin_potions()
    elif choix_objet == '2':
        if argent >= 250:
            print("\nVous avez acheté une potion de magie.")
            Magie += 10
            argent -= 250
            if Magie >= 20: 
                Magie = 20
            magasin_potions()
        else:
            print("\nVous n'avez pas assez d'argent pour acheter cette potion.")
            magasin_potions()
    elif choix_objet == '3':
        if argent >= 50:
            print("\nVous avez acheté une potion de vie.")
            Vie += 10
            argent -= 50
            if Vie >= 20: 
                Vie = 20
            magasin_potions()
        else:
            print("\nVous n'avez pas assez d'argent pour acheter cette potion.")
            magasin_potions()
    elif choix_objet == '4':
        if argent >= 300:
            print("\nVous avez acheté une potion de transformation.")
            print("\nVous la buvez et vous sentez votre corps changer.")
            changer_personnage()
        else:
            print("\nVous n'avez pas assez d'argent pour achter cette potion.")
            magasin_potions()
    elif choix_objet == '5':
        if argent >= 1000:
            if dragon is False:
                print("\nVous avez acheté une potion de transformation en dragon.")
                print("Vous la buvez et vous sentez votre corps changer. Votre corps se couvre d'écailles et vous vous transformez en dragon en un éclair de lumière.")
                personnage = "Dragon"
                caractéristiques = "Maîtrise la magie, possède des sorts spéciaux"
                Force = 20
                Défense = 20
                Intelligence = 20
                Adresse = 20
                Magie = 20
                Vie = 20
                dragon = True
                argent -= 1000
                print(f"Vous êtes maintenant un {personnage}.")
                print(f"Caractéristiques : {caractéristiques}, Force : {Force}, Intelligence : {Intelligence}, Adresse : {Adresse}, Magie : {Magie}, Vie : {Vie}.")
                magasin_potions()
            else: 
                print("\nVous êtes déjà un dragon.")
                magasin_potions()
        else: 
            print("\nVous n'avez pas assez d'argent pour acheter cette potion.")
            magasin_potions()
    elif choix_objet == '6':
        magasin()
    else:
        print("\nChoix invalide. Veuillez sélectionner un numéro entre 1 et 5.")
        magasin_potions()

# Menu principal
def menu_principal():
    global emplacement_actuel
    emplacement_actuel = 'Menu principal'
    print("\n--- Menu Principal ---")
    print("Vous êtes à la croisée des chemins, que voulez-vous faire ?")
    print("1. Aller à Ravenwood.")
    print("2. Aller à Tryndamere.")
    print("3. Aller à Mordor.")
    print("4. Aller au magasin.")
    print("5. Charger une sauvegarde.")
    print("6. Sauvegarder et continuer.")
    print("7. Gérer les sauvegardes.")
    print("8. Quitter le jeu.")
    choix = input("Entrez le numéro de votre choix (Entre 1 et 7) : ")
    if choix == '1':
        print("\nVous allez à Ravenwood.")
        ravenwood()
    elif choix == '2':
        print("\nVous allez à Tryndamere.")
        tryndamere()
    elif choix == '3':
        print("\nVous allez à Mordor.")
        mordor()
    elif choix == '4':
        print("Vous allez au magasin.")
        magasin()
    elif choix == '5':
        choix = input("\nVoulez vous sauvegarder avant de charger une sauvegarde ?")
        if choix.lower == 'oui':
            sauvegarder_jeu()
            début_du_jeu()
        elif choix.lower == 'non':
            début_du_jeu()
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.")
            menu_principal()
    elif choix == '6':
        choix = input("\nVoulez vous sauvegarder ? (oui/non) : ")
        if choix.lower() == 'oui':
            sauvegarder_jeu()
            reprendre_jeu()
        elif choix.lower() == 'non':
            menu_principal()
    elif choix == '7':
        gerer_les_sauvegardes()
    elif choix == '8':
        choix = input("\nVoulez vous sauvegarder ? (oui/non) : ")
        if choix.lower() == 'oui':
            sauvegarder_jeu()
            print("Merci d'avoir joué !\n")
            exit()
        elif choix.lower() == 'non':
            print("Merci d'avoir joué !\n")
            exit()
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.")
            menu_principal()
    else: 
        print("\nChoix invalide. Veuillez sélectionner une option valide.")
        menu_principal()

#Fonction de la première quête
def premiere_quete():
    global Première_Quête
    Première_Quête = False
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    print("\n--- Des gobelins à Ravenwood ---\n")
    print(
        "Maire : 'Aventurier, notre village est attaqué par des gobelins ! Pouvez-vous nous aider à les chasser ?'"
    )
    print("\nQue voulez-vous répondre ?")
    print("1. Oui, je vais vous aider.")
    print("2. Non, je ne suis pas intéressé par cette mission.")
    choix = input("Entrez le numéro de votre choix (1 ou 2) : ")

    if choix == '1':
        print("\nVous : 'Oui, je vais vous aider.'")
        print(
            "Maire : 'Merci beaucoup ! Les gobelins se cachent dans la grotte au nord du village. Bonne chance, aventurier.'"
        )

        print("\nVous vous dirigez vers la grotte au nord du village.")
        print(
            "À l'entrée de la grotte, vous voyez plusieurs gobelins. Vous devez maintenant décider comment les affronter."
        )

        # Choix de la stratégie
        if dragon is False:
            print("\nQuelle stratégie voulez-vous utiliser ?")
            print("1. Attaquer de front avec toute votre force.")
            print(
                "2. Utiliser la magie pour les affaiblir avant de les attaquer."
            )
            print("3. Utiliser la discrétion pour les surprendre.")
            choix_strategie = input(
                "Entrez le numéro de votre choix (1, 2 ou 3) : ")
        else:
            print("\nQuelle stratégie voulez-vous utiliser ?")
            print("1. Attaquer de front avec toute votre force.")
            print(
                "2. Utiliser la magie pour les affaiblir avant de les attaquer."
            )
            print("3. Utiliser la discrétion pour les surprendre.")
            print("4. Leur cracher des flammes pour les brûler.")
            print("5. Les attaquer avec vos crocs.")
            choix_strategie = input(
                "Entrez le numéro de votre choix (1, 2, 3, 4 ou 5) : ")

        if choix_strategie == '1':
            Dé = random.randint(1, 20)
            if Dé <= Force:
                print("\nVous décidez d'attaquer de front avec toute votre force.")
                print("Grâce à votre puissance, vous parvenez à vaincre les gobelins.")
            else:
                print("\nVous décidez d'attaquer de front avec toute votre force.")
                print("Cependant, les gobelins sont trop nombreux et vous êtes submergé. Vous devez battre en retraite et repenser votre stratégie.")
                Dé = random.randint(1, 10)
                Dégât = Dé
                Vie -= Dégât
                print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                verifier_vie()
        elif choix_strategie == '2':
            Dé = random.randint(1, 20)
            if Dé <= Magie:
                print("\nVous utilisez votre magie pour affaiblir les gobelins avant de les attaquer.")
                print("Votre plan fonctionne parfaitement et vous parvenez à vaincre les gobelins.")
            else:
                print("\nVous tentez d'utiliser votre magie pour affaiblir les gobelins.")
                print("Malheureusement, votre magie n'est pas assez puissante et vous êtes submergé. Vous devez battre en retraite et repenser votre stratégie.")
                Dé = random.randint(1, 10)
                Dégât = Dé
                Vie -= Dégât
                print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                verifier_vie()
        elif choix_strategie == '3':
            Dé = random.randint(1, 20)
            if Dé <= Adresse:
                print("\nVous décidez d'utiliser la discrétion pour surprendre les gobelins.")
                print("Votre plan fonctionne parfaitement et vous parvenez à vaincre les gobelins.")
            else:
                print("\nVous tentez d'utiliser la discrétion pour surprendre les gobelins.")
                print("Malheureusement, votre tentative échoue et vous êtes repéré. Vous devez battre en retraite et repenser votre stratégie.")
                Dé = random.randint(1, 10)
                Dégât = Dé
                Vie -= Dégât
                print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                verifier_vie()
        elif choix_strategie == '4':
            if dragon is True:
                print("\nVous crachez des flammes sur les gobelins.")
                print("Votre plan fonctionne parfaitement et vous parvenez à vaincre les gobelins.")
            else:
                print("Choix invalide. Veuillez choisir une stratégie valide.")
                premiere_quete()
        elif choix_strategie == '5':
            if dragon is True:
                print("\nVous attaquez les gobelins avec vos crocs.")
                print("Votre plan fonctionne parfaitement et vous parvenez à vaincre les gobelins.")
            else:
                print("Choix invalide. Veuillez choisir une stratégie valide.")
                premiere_quete()
        else:
            print("\nChoix invalide. Veuillez sélectionner une stratégie valide.")
            premiere_quete()

        print("\nFélicitations ! Vous avez réussi la quête 'Des gobelins à Ravenwood' et avez débarrassé la grotte des gobelins.")
        print("Le village de Rivenwood vous est reconnaissant pour votre aide.")
        Première_Quête = True
        gain = random.randint(50, 100)
        print("Vous recevez une récompense de " + str(gain) + " pièces d'or.")
        global argent
        argent += gain
        ravenwood()
    else:
        print("\nVous : 'Non, je ne suis pas intéressé par cette mission.'")
        print("Maire : 'Je comprends, aventurier. Merci quand même.'")
        ravenwood()

    return "Première quête terminée.", Première_Quête


#Fonction de la deuxième quête
def deuxieme_quete():
    global Deuxième_Quête
    Deuxième_Quête = False
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    print("\n--- Les objets volés ---\n")
    print("Maire : 'Merci beaucoup pour votre aide, aventurier. Cependant, nous avons encore besoin de votre aide.'")
    print("Maire : 'Récemment, des objets précieux ont été volés dans notre village. Nous soupçonnons une bande de voleurs qui se cache dans la forêt.'")
    print("Maire : 'Pouvez-vous retrouver les objets volés et arrêter ces voleurs ?'")
    print("\nQue voulez-vous répondre ?")
    print("1. Oui, je vais vous aider à retrouver les objets volés.")
    print("2. Non, je ne suis pas intéressé par cette mission.")
    choix = input("Entrez le numéro de votre choix (1 ou 2) : ")
    if choix == '1':
        print("\nVous : 'Oui, je vais vous aider à retrouver les objets volés.'")
        print("Maire : 'Merci infiniment ! Les voleurs se cachent quelque part dans la forêt au nord du village. Bonne chance, aventurier.'")
        print("\nVous vous dirigez vers la forêt au nord du village.")
        print("Après quelques heures de recherche, vous repérez un groupe de personnes suspectes cachées dans un campement.")
        print("Vous devez maintenant décider comment les affronter.")

        # Choix de la stratégie
        if not dragon:
            print("\nQuelle stratégie voulez-vous utiliser ?")
            print("1. Attaquer de front avec toute votre force.")
            print("2. Utiliser la magie pour les immobiliser avant de les attaquer.")
            print("3. Utiliser la discrétion pour les surprendre et récupérer les objets volés.")
            choix_strategie = input("Entrez le numéro de votre choix (1, 2 ou 3) : ")
        else:
            print("\nQuelle stratégie voulez-vous utiliser ?")
            print("1. Attaquer de front avec toute votre force.")
            print("2. Utiliser la magie pour les immobiliser avant de les attaquer.")
            print("3. Utiliser la discrétion pour les surprendre et récupérer les objets volés.")
            print("4. Les brûler en leur crachant des flammes mortelles.")
            print("5. Utiliser ses crocs pour les neutraliser.")
            choix_strategie = input("Entrez le numéro de votre choix (1, 2, 3, 4 ou 5) : ")

            if choix_strategie == '1':
                Dé = random.randint(1, 20)
                if Dé <= Force:
                    print("\nVous décidez d'attaquer de front avec toute votre force.")
                    print("Grâce à votre puissance, vous parvenez à vaincre les voleurs et à récupérer les objets volés.")
                else:
                    print("\nVous décidez d'attaquer de front avec toute votre force.")
                    print("Cependant, les voleurs sont trop nombreux et vous êtes submergé. Vous devez battre en retraite et repenser votre stratégie.")
                    Dé = random.randint(1, 10)
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix_strategie == '2':
                Dé = random.randint(1, 20)
                if Dé <= Magie:
                    print("\nVous utilisez votre magie pour immobiliser les voleurs avant de les attaquer.")
                    print("Votre plan fonctionne parfaitement et vous parvenez à vaincre les voleurs et à récupérer les objets volés.")
                else:
                    print("\nVous tentez d'utiliser votre magie pour immobiliser les voleurs.")
                    print("Malheureusement, votre magie n'est pas assez puissante et vous êtes submergé. Vous devez battre en retraite et repenser votre stratégie.")
                    Dé = random.randint(1, 10)
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix_strategie == '3':
                Dé = random.randint(1, 20)
                if Dé <= Adresse:
                    print("\nVous décidez d'utiliser la discrétion pour surprendre les voleurs et récupérer les objets volés.")
                    print("Votre plan fonctionne parfaitement et vous parvenez à récupérer les objets volés sans être repéré.")
                else:
                    print("\nVous tentez d'utiliser la discrétion pour surprendre les voleurs.")
                    print("Malheureusement, votre tentative échoue et vous êtes repéré. Vous devez battre en retraite et repenser votre stratégie.")
                    Dé = random.randint(1, 10)
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix_strategie == '4':
                if dragon:
                    print("\nVous décidez de brûler les voleurs en leur crachant des flammes mortelles.")
                    print("Votre tactique est très efficace et vous parvenez à vaincre les voleurs et à récupérer les objets volés.")
                else:
                    print("\nChoix invalide. Vous devez choisir une stratégie valide.")
                    deuxieme_quete()
            elif choix_strategie == '5':
                if dragon:
                    print("\nVous décidez d'utiliser vos crocs pour neutraliser les voleurs.")
                    print("Votre force et votre férocité vous permettent de vaincre facilement les voleurs et de récupérer les objets volés.")
                else:
                    print("\nChoix invalide. Vous devez choisir une stratégie valide.")
                    deuxieme_quete()
            else:
                print("\nChoix invalide. Veuillez sélectionner une stratégie valide.")
                deuxieme_quete()

        print("\nFélicitations ! Vous avez réussi la quête 'Les objets volés' et avez récupéré les objets volés.")
        print("Le village de Rivenwood vous est reconnaissant pour votre aide.")
        Deuxième_Quête = True
        gain = random.randint(50, 100)
        print("Vous recevez une récompense de " + str(gain) + " pièces d'or.")
        global argent
        argent += gain
        ravenwood()
    else:
        print("\nVous : 'Non, je ne suis pas intéressé par cette mission.'")
        print("Maire : 'Je comprends, aventurier. Merci quand même.'")
        ravenwood()

    return "Deuxième quête terminée.", Deuxième_Quête


# Fonction pour la troisième quête
def troisieme_quete():
    global Troisième_Quête
    Troisième_Quête = False
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    print("\n--- Le démon de Ravenwood ---\n")
    print("Maire : 'Merci beaucoup pour votre aide, aventurier. Cependant, nous avons encore besoin de votre aide une dernière fois.'")
    print("Maire : 'Un démon terrifiant est apparu dans les montagnes et menace notre village. Pouvez-vous le vaincre ?'")
    print("\nQue voulez-vous répondre ?")
    print("1. Oui, je vais affronter ce démon.")
    print("2. Non, cette tâche est trop dangereuse pour moi.")
    choix = input("Entrez le numéro de votre choix (1 ou 2) : ")
    if choix == '1':
        print("\nVous : 'Oui, je vais affronter ce démon.'")
        print("Maire : 'Merci infiniment ! Le démon se cache dans les montagnes à l'est du village. Bonne chance, aventurier.'")
        print("\nVous vous dirigez vers les montagnes à l'est du village.")
        print("Après une longue ascension, vous trouvez enfin la tanière du démon.")
        print("Vous devez maintenant décider comment l'affronter.")

        # Choix de la stratégie
        if not dragon:
            print("\nQuelle stratégie voulez-vous utiliser ?")
            print("1. Attaquer de front avec toute votre force.")
            print("2. Utiliser la magie pour l'affaiblir avant de l'attaquer.")
            print("3. Piéger le démon et l'attaquer par surprise.")
            choix_strategie = input("Entrez le numéro de votre choix (1, 2 ou 3) : ")
        else:
            print("\nQuelle stratégie voulez-vous utiliser ?")
            print("1. Attaquer de front avec toute votre force.")
            print("2. Utiliser la magie pour l'affaiblir avant de l'attaquer.")
            print("3. Piéger le démon et l'attaquer par surprise.")
            print("4. Utiliser votre souffle de feu pour l'affaiblir.")
            print("5. Utiliser vos crocs pour attaquer le démon.")
            choix_strategie = input("Entrez le numéro de votre choix (1, 2, 3, 4 ou 5) : ")

            if choix_strategie == '1':
                Dé = random.randint(1, 20)
                if Dé <= Force:
                    print("\nVous décidez d'attaquer de front avec toute votre force.")
                    print("Grâce à votre puissance, vous parvenez à vaincre le démon après un combat acharné.")
                else:
                    print("\nVous décidez d'attaquer de front avec toute votre force.")
                    print("Cependant, le démon est trop puissant et vous êtes submergé. Vous devez battre en retraite et repenser votre stratégie.")
                    Dé = random.randint(1, 10)
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix_strategie == '2':
                Dé = random.randint(1, 20)
                if Dé <= Magie:
                    print("\nVous utilisez votre magie pour affaiblir le démon avant de l'attaquer.")
                    print("Votre plan fonctionne parfaitement et vous parvenez à vaincre le démon après un combat intense.")
                else:
                    print("\nVous tentez d'utiliser votre magie pour affaiblir le démon.")
                    print("Malheureusement, le démon est trop puissant et vous êtes submergé. Vous devez battre en retraite et repenser votre stratégie.")
                    Dé = random.randint(1, 10)
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix_strategie == '3':
                Dé = random.randint(1, 20)
                if Dé <= Adresse:
                    print("\nVous décidez de piéger le démon et de l'attaquer par surprise.")
                    print("Votre plan fonctionne parfaitement et vous parvenez à vaincre le démon après un combat acharné.")
                else:
                    print("\nVous tentez de piéger le démon et de l'attaquer par surprise.")
                    print("Malheureusement, votre tentative échoue et vous êtes repéré. Vous devez battre en retraite et repenser votre stratégie.")
                    Dé = random.randint(1, 10)
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix_strategie == '4':
                if dragon:
                    print("\nVous décidez d'utiliser votre souffle de feu pour affaiblir le démon.")
                    print("Votre souffle de feu est très efficace et vous parvenez à vaincre le démon après un combat épique.")
                else:
                    print("\nChoix invalide. Vous devez choisir une stratégie valide.")
                    troisieme_quete()
            elif choix_strategie == '5':
                if dragon:
                    print("\nVous décidez d'utiliser vos crocs pour attaquer le démon.")
                    print("Votre force et votre férocité vous permettent de vaincre le démon après un combat acharné.")
                else:
                    print("\nChoix invalide. Vous devez choisir une stratégie valide.")
                    troisieme_quete()
            else:
                print("\nChoix invalide. Veuillez sélectionner une stratégie valide.")
                troisieme_quete()

        print("\nFélicitations ! Vous avez réussi la quête 'Le démon de Ravenwood' et avez vaincu le démon.")
        print("Le village de Ravenwood est enfin en sécurité grâce à vous.")
        Troisième_Quête = True
        gain = random.randint(50, 100)
        print("Vous recevez une récompense de " + str(gain) + " pièces d'or.")
        global argent
        argent += gain
        ravenwood()
    else:
        print("\nVous : 'Non, cette tâche est trop dangereuse pour moi.'")
        print("Maire : 'Je comprends, aventurier. Merci pour tout ce que vous avez déjà fait pour notre village.'")
        ravenwood()

    return "Troisième quête terminée.", Troisième_Quête


#Fonction pour choisir la quête à Ravenwood
def ravenwood():
    global Première_Quête
    global Deuxième_Quête
    global Troisième_Quête
    global emplacement_actuel
    emplacement_actuel = 'Ravenwood'
    if Première_Quête is False:
        print("\nVous êtes à Ravenwood. Vous avez une quête à faire :")
        print("---Que voulez-vous faire ?---")
        print("1. Commencer la quête 'Des gobelins à Ravenwood'.")
        print("2. Quitter le village.")
        choix = input("Entrez le numéro de votre choix (1 ou 2): ")
        if choix == '1':
            if Première_Quête is False:
                premiere_quete()
            else: 
                print("\nTu as déjà fait cette quête.")
                ravenwood()
        elif choix == '2':
            print("Vous quittez le village de Ravenwood.")
            menu_principal()
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.")
            ravenwood()
            return "Ravenwood"
    elif Première_Quête is True and Deuxième_Quête is False:
        print("\nVous êtes à Ravenwood. Vous avez deux quêtes à faire :")
        print("---Que voulez-vous faire ?---")
        print("1. Commencer la quête 'Des gobelins à Ravenwood'.")
        print("2. Commencer la quête 'Les objets volés'.")
        print("3. Quitter le village.")
        choix = input("Entrez le numéro de votre choix (1 ou 2): ")
        if choix == '1':
            if Première_Quête is False:
                premiere_quete()
            else: 
                print("\nTu as déjà fait cette quête.")
                ravenwood()
        elif choix == '2':
            if Première_Quête is True and Deuxième_Quête is False:
                deuxieme_quete()
            elif Première_Quête is False:
                print("\nTu n'as pas fait la quête précédente. Retente ta chance.")
                ravenwood()
            else:
                print("\nTu as déjà fait cette quête.")
                ravenwood()
        elif choix == '3':
            print("Vous quittez le village de Ravenwood.")
            menu_principal()
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.")
            ravenwood()
            return "Ravenwood"
    elif Deuxième_Quête is True and Troisième_Quête is False:
        print("\nVous êtes à Ravenwood. Vous avez trois quêtes à faire :")
        print("---Que voulez-vous faire ?---")
        print("1. Commencer la quête 'Des gobelins à Ravenwood'.")
        print("2. Commencer la quête 'Les objets volés'.")
        print("3. Commencer la quête 'Le Démon de Ravenwood'.")
        print("4. Quitter le village.")
        choix = input("Entrez le numéro de votre choix (Entre 1 et 3) : ")
        if choix == '1':
            if Première_Quête is False:
                premiere_quete()
            else: 
                print("\nTu as déjà fait cette quête.")
                ravenwood()
        elif choix == '2':
            if Première_Quête is True and Deuxième_Quête is False:
                deuxieme_quete()
            elif Première_Quête is False:
                print("\nTu n'as pas fait la quête précédente. Retente ta chance.")
                ravenwood()
            else:
                print("\nTu as déjà fait cette quête.")
                ravenwood()
        elif choix == '3':
            if Deuxième_Quête is True and Troisième_Quête is False:
                troisieme_quete()
            elif Deuxième_Quête is False:
                print("\nTu n'as pas fait la quête précédente. Retente ta chance.")
                ravenwood()
            else:
                print("\nTu as déjà fait cette quête.")
                menu_principal()
        elif choix == '4':
            menu_principal()
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.")
            ravenwood()
            return "Ravenwood"
    else:
        print("\nVous êtes à Ravenwood. Vous avez déjà fait toutes les quêtes du village.")
        print("Vous retournez à la croisée des chemins.")
        menu_principal()
        return "Ravenwood"

#Fonction pour la deuxième partie de la quatrième quête
def quatrieme_quete_partie_2():
    global Quatrième_Quête
    Quatrième_Quête = False
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    if not dragon:
        print("\nVous faites face au groupe de pillards ainsi qu'au géant.")
        print("\nQuelle stratégie voulez-vous adopter ?")
        print("1. Attaquer de front avec toute votre force.")
        print("2. Utiliser la magie pour attaquer.")
        print("3. Piéger minutieusement le groupe de pillards et l'attaquer par surprise.")
        print("4. Faire preuve d'adresse afin d'utiliser une réaction en chaîne pour tous les neutraliser.")
        choix = input("Entrez le numéro de votre choix (1, 2, 3 ou 4) : ")
    else:
        print("\nVous faites face au groupe de pillards ainsi qu'au géant.")
        print("\nQuelle stratégie voulez-vous adopter ?")
        print("1. Attaquer de front avec toute votre force.")
        print("2. Utiliser la magie pour attaquer.")
        print("3. Piéger minutieusement le groupe de pillards et l'attaquer par surprise.")
        print("4. Faire preuve d'adresse afin d'utiliser une réaction en chaîne pour tous les neutraliser.")
        print("5. Vous vous envolez et vous allez planter vos crocs dans la gorge du géant pour le tuer puis vous descendez, vous volez en rase-mottes en crachant des flammes sur les pillards.")
        choix = input("Entrez le numéro de votre choix (1, 2, 3, 4 ou 5) : ")

    if choix == '1':
        Dé = random.randint(1, 20)
        if Dé <= Force:
            print("\nVous décidez d'attaquer de front avec toute votre force.")
            print("Grâce à votre puissance, vous parvenez à vaincre le groupe de pillards après un combat acharné.")
            print("Le géant, ne sachant quoi faire se suicide.")
        else:
            print("\nVous décidez d'attaquer de front avec toute votre force.")
            print("Cependant, le groupe de pillards est trop puissant et vous êtes submergé. Vous devez battre en retraite et repenser votre stratégie.")
            Dé = random.randint(1, 10)
            Dégât = Dé
            Vie -= Dégât
            print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
            verifier_vie()
    elif choix == '2':
        Dé = random.randint(1, 20)
        if Dé <= Magie:
            print("\nVous utilisez votre magie pour attaquer.")
            print("Votre plan fonctionne parfaitement et vous parvenez à vaincre le groupe de pillards après un combat intense.")
            print("Le géant, ne sachant quoi faire se suicide.")
        else:
            print("\nVous tentez d'utiliser votre magie pour attaquer.")
            print("Malheureusement, votre magie n'est pas assez puissante et vous êtes submergé. Vous devez battre en retraite et repenser votre stratégie.")
            Dé = random.randint(1, 10)
            Dégât = Dé
            Vie -= Dégât
            print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
            verifier_vie()
    elif choix == '3':
        Dé = random.randint(1, 20)
        if Dé <= Intelligence:
            print("\nVous décidez de piéger le groupe de pillards et de l'attaquer par surprise.")
            print("Votre plan fonctionne parfaitement et vous parvenez à vaincre le groupe de pillards après un combat acharné.")
            print("Le géant, ne sachant quoi faire se suicide.")
        else:
            print("\nVous tentez de piéger le groupe de pillards et de l'attaquer par surprise.")
            print("Malheureusement, votre tentative échoue et vous êtes repéré. Vous devez battre en retraite et repenser votre stratégie.")
            Dé = random.randint(1, 10)
            Dégât = Dé
            Vie -= Dégât
            print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
            verifier_vie()
    elif choix == '4':
        Dé = random.randint(1, 20)
        if Dé <= Adresse:
            print("\nVous décidez de faire preuve d'adresse afin d'utiliser une réaction en chaîne pour tous les neutraliser.")
            print("Votre plan fonctionne parfaitement et vous parvenez à vaincre le groupe de pillards après un combat acharné.")
            print("Le géant, ne sachant quoi faire se suicide.")
        else:
            print("\nVous tentez de faire preuve d'adresse afin de tous les neutraliser.")
            print("Malheureusement, votre tentative échoue et vous êtes repéré. Vous devez battre en retraite et repenser votre stratégie.")
            Dé = random.randint(1, 10)
            Dégât = Dé
            Vie -= Dégât
            print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
            verifier_vie()
    elif choix == '5':
        if dragon:
            print("\nVous vous envolez et vous allez planter vos crocs dans la gorge du géant pour le tuer puis vous descendez, vous volez en rase-mottes en crachant des flammes sur les pillards.")
            print("Votre plan fonctionne parfaitement et vous parvenez à vaincre le groupe de pillards après un combat acharné.")
        else:
            print("\nChoix invalide. Vous devez choisir une stratégie valide.")
            quatrieme_quete_partie_2()
    else:
        print("\nChoix invalide. Veuillez sélectionner une option valide.")
        quatrieme_quete_partie_2()

    print("\nFélicitations ! Vous avez réussi la quête 'Les Pillards de Tryndamere'.")
    print("Vous avez enfin éliminé tous les pillards et le géant.")
    print("Vous avez sauvé la ville de Tryndamere.")
    gain = random.randint(75, 150)
    print("Vous recevez une récompense de " + str(gain) + " pièces d'or.")
    Quatrième_Quête = True
    global argent
    argent += gain
    tryndamere()
    return "Quatrième Quête terminée", Quatrième_Quête


#Fonction pour la quatrième quête
def quatrieme_quete():
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global dragon
    global Quatrième_Quête_partie1
    Quatrième_Quête_partie1 = False
    print("\n--- Les Pillards de Tryndamere ---\n")
    print("Le maire de la ville vous demande de l'aider à résoudre un mystère.")
    print("Maire : 'Une bande de pillards a ravagée la ville avec l'appui d'un géant. Nous avons réussi à leur coller un traceur magique sur la semelle de l'un d'entre eux.'")
    print("Maire : 'Voulez vous nous aider ?'")
    print("\nQue voulez-vous répondre ?")
    print("1. Oui, je vais aider vous aider.")
    print("2. Non, je ne peux pas vous aider.")
    choix = input("Entrez le numéro de votre choix (1 ou 2) : ")
    if choix == '1':
        print("Vous : 'Oui, je vais aider vous aider.'")
        print("Maire : 'Merci beaucoup ! Nous avons besoin de votre aide pour retrouver les pillards et les battre.'")
        print("Le maire vous donne une carte où un point rouge se déplace en clignotant.")
        print("Vous suivez la carte et vous arrivez au pied d'une montagne.")
        if dragon is False:
            print("\n---Que voulez-vous faire ?---")
            print("1. Vous décidez d'escalader la montagne pour arriver chez les pillards.")
            print("2. Vous décidez d'utiliser votre magie pour arriver au sommet de la montagne.")
            print("3. Vous décidez d'utiliser un miroir pour envoyer des signaux lumineux afin de faire descendre les pillards.")
            choix = input("Entrez le numéro de votre choix (1, 2 ou 3) : ")
        else:
            print("\n---Que voulez-vous faire ?---")
            print("1. Vous décidez d'escalader la montagne pour arriver chez les pillards.")
            print("2. Vous décidez d'utiliser votre magie pour arriver au sommet de la montagne.")
            print("3. Vous décidez d'utiliser un miroir pour envoyer des signaux lumineux afin de faire descendre les pillards.")
            print("4. Vous vous envolez pour le sommet.")
            choix = input("Entrez le numéro de votre choix (Entre 1 et 4) : ")
        while Quatrième_Quête_partie1 is False:
            if choix == '1':
                Dé = random.randint(1, 20)
                if Dé <= Force:
                    print("\nVous décidez d'escalader la montagne pour arriver chez les pillards.")
                    Quatrième_Quête_partie1 = True
                    quatrieme_quete_partie_2()
                else:
                    print("\nVous tentez d'escalader la montagne pour arriver chez les pillards.")
                    print("Malheureusement, la pente est trop raide et vous échouez. Vous devez repenser votre stratégie.")
                    quatrieme_quete()
            elif choix == '2':
                Dé = random.randint(1, 20)
                if Dé <= Magie:
                    print("\nVous utilisez votre magie pour arriver au sommet de la montagne.")
                    print("Votre plan fonctionne parfaitement et vous parvenez à arriver chez les pillards.")
                    Quatrième_Quête_partie1 = True
                    quatrieme_quete_partie_2()
                else:
                    print("\nVous tentez d'utiliser votre magie pour arriver au sommet de la montagne.")
                    print("Malheureusement, votre magie n'est pas assez puissante et vous échouez. Vous devez repenser votre stratégie.")
                    quatrieme_quete()
            elif choix == '3':
                Dé = random.randint(1, 20)
                if Dé <= Intelligence:
                    print("\nVous utilisez un miroir pour envoyer des signaux lumineux afin de faire descendre les pillards.")
                    print("Votre plan fonctionne parfaitement et vous parvenez à arriver chez les pillards.")
                    Quatrième_Quête_partie1 = True
                    quatrieme_quete_partie_2()
                else:
                    print("\nVous tentez d'utiliser un miroir pour envoyer des signaux lumineux afin de faire descendre les pillards.")
                    print("Malheureusement, votre magie n'est pas assez puissante et vous échouez. Vous devez repenser votre stratégie.")
                    quatrieme_quete()
            elif choix == '4':
                if dragon:
                    print("\nVous vous envolez pour le sommet.")
                    print("Votre force et votre férocité vous permettent de faire descendre les pillards.")
                    Quatrième_Quête_partie1 = True
                    quatrieme_quete_partie_2()
                else:
                    print("\nChoix invalide. Vous devez choisir une stratégie valide.")
                    quatrieme_quete()
            else:
                print("\nChoix invalide. Veuillez sélectionner une option valide.")
                quatrieme_quete()
    elif choix == '2':
        print("Vous : 'Non je ne vais pas vous aider.'")
        print("Maire : 'Je comprends, aventurier. Merci pour votre compréhension.'")
        menu_principal()
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
        quatrieme_quete()

    return "Première partie de la quatrième quête terminée.", Quatrième_Quête_partie1


#Fonction pour la cinquième quête
def cinquieme_quete():
    global Cinquième_Quête
    Cinquième_Quête = False
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    print("\n--- Les Trolls du pont ---\n")
    print("Maire : 'Merci d'avoir arrêté les pillards et le géant qui les accompagnait.")
    print("Vous : 'Ce n'est rien.'")
    print("Maire : 'Nous avons encore besoin de votre aide.'")
    print("Maire : 'Des trolls barrent l'accès du pont et empêche les personnes et les marchandises de passer. Il faut les déloger pour que la ville puisse de nouveau être prospère.'")
    print("\n--- Que voulez-vous répondre ? ---")
    print("1. Oui bien sûr.")
    print("2. Non, j'en ai assez fait pour vous.")
    choix = input("Entrez le numéro de votre choix (1 ou 2) : ")
    if choix == '1':
        print("Vous : 'Bien sûr. Pouvez-vous me donner les indications nécessaires ?'")
        print("Maire : 'Merci monseigneur.'")
        print("Le maire vous donne une carte et vous désigne le pont où se trouvent les trolls.")
        print("Vous quittez le village et vous partez en direction du pont indiqué sur la carte.")
        print("Les trolls vous accueillent et vous posent une question.")
        print("Trolls : 'Voulez vous résoudre une énigme ?'")
        print("Vous ne voulez pas écouter son énigme.")
        print("\nVous décidez d'attaquer les trolls.")
        if not dragon:
            print("--- Comment voulez-vous procéder ? ---")
            print("1. Foncer dans le tas et advienne que pourra.")
            print("2. Les ensorceler pour les vaincre.")
            print("3. Faire s'effondrer le pont sur les trolls.")
            choix = input("Entrer le numéro de votre choix (1, 2 ou 3) : ")
        else:
            print("--- Comment voulez-vous procéder ? ---")
            print("1. Foncer dans le tas et advienne que pourra.")
            print("2. Les ensorceler pour les vaincre.")
            print("3. Faire s'effondrer le pont sur les trolls.")
            print("4. Les brûler impitoyablement.")
            print("5. Leur planter les crocs dans la chair.")
            choix = input("Entrer le numéro de votre choix (Entre 1 et 5) : ")
            
        if choix == '1':
            Dé = random.randint(1, 20)
            if Dé <= Force:
                print("Vous foncez dans le tas et vous éliminez tous les trolls.")
                print("Vous retournez à la ville de Tryndamere en héros.")
            else:
                print("Vous foncez dans le tas mais vous vous faites submerger.")
                print("Vous battez en retraite.")
                Dé = random.randint(1, 10)
                Dégât = Dé
                Vie -= Dégât
                print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                verifier_vie()
        elif choix == '2':
            Dé = random.randint(1, 20)
            if Dé <= Magie:
                print("Vous ensorcelez les trolls avec succès et ils tombent dans la rivière.")
                print("Vous retournez à la ville de Tryndamere en héros.")
            else:
                print("Vous tentez de les ensorceler mais ça ne fonctionne pas.")
                print("Vous battez en retraite.")
                Dé = random.randint(1, 10)
                Dégât = Dé
                Vie -= Dégât
                print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                verifier_vie()
        elif choix == '3':
            Dé = random.randint(1, 20)
            if Dé <= Intelligence:
                print("Vous faites s'effondrer le pont sur les trolls et vous les éliminez tous.")
                print("Vous retournez à la ville de Tryndamere en héros.")
            else:
                print("Vous tentez de faire s'écrouler le pont mais vous n'y parvenez pas.")
                print("Vous battez en retraite.")
                Dé = random.randint(1, 10)
                Dégât = Dé
                Vie -= Dégât
                print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                verifier_vie()
        elif choix == '4':
            if dragon is True: 
                print("Vous brûlez les trolls qui se retrouvent réduis à un pauvre tas de cendres.")
                print("Vous retournez à la ville de Tryndamere en héros.")
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                cinquieme_quete()
        elif choix == '5':
            if dragon is True: 
                print("Vous plantez vos crocs dans la chair des trolls ce qui les tue sur le coup.")
                print("Vous retournez à la ville de Tryndamere en héros.")
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                cinquieme_quete()
    elif choix == '2':
        print("Vous : 'Non, je pense que j'en ai assez fait pour vous. Débrouillez vous. Au revoir.")
        print("Maire : 'Mais monseigneur...'")
        tryndamere()
    else:
        print("Choix invalide, veuillez réessayer.")
        cinquieme_quete()
    
    print("\nFélicitations ! Vous avez réussi la quête 'Les Trolls du pont'.")
    print("Vous avez débarassé le pont des trolls et le commerce a pu reprendre.")
    print("Vous avez sauvé la ville de Tryndamere.")
    gain = random.randint(50, 100)
    print("Vous recevez une récompense de " + str(gain) + " pièces d'or.")
    Cinquième_Quête = True
    argent += gain
    tryndamere()

    return "Cinquième quête terminée.", Cinquième_Quête

# Fonction pour la sixième quête
def sixieme_quete():
    global Sixième_Quête
    Sixième_Quête = False
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    print("\n--- Les Fées de l'étang ---\n")
    print("\nLe maire de Tryndamere vous remercie encore chaleureusement pour avoir débarassé le pont de ses trolls.")
    print("Maire : 'Nous avons un autre problème.'")
    print("Maire : 'Pouvez vous nous aider ?'")
    print("\n--- Que voulez-vous répondre ? ---\n")
    print("1. Oui je peux.")
    print("2. Non je n'ai pas envie.")
    choix = input("Entrez le numéro de votre choix (1 ou 2) : ")
    if choix == '1':
        if not dragon:
                print("\nVous : 'Oui monsieur le maire je serai ravi de pouvoir vous aider à nouveau.'")
                print("Maire : 'Merci, je savais que je pouvais compter sur vous.'")
                print("Maire : 'Des fées malintentionnées nous font chanter. Nous comptons sur vous pour nous aider. Elles habitent dans un étang situé non-loin de la ville.'")
                print("\nVous partez en direction de l'étang que le maire vous a indiqué.")
                print("Vous y trouvez les fées en train de barboter au bord de l'eau.")
                print("Les fées vous voient et comprennent aussitôt pourquoi vous êtes là. Il faut agir vite.")
                print("\n--- Que voulez-vous faire ? ---")
                print("1. Vous décidez d'utiliser la magie.")
                print("2. Vous décidez de passer en force.")
                print("3. Vous faites preuve d'ingéniosité.")
                choix = input("Entrez le numéro de votre choix (entre 1 et 3) : ")
        else:
            print("\nVous : 'Oui monsieur le maire je serai ravi de pouvoir vous aider à nouveau.'")
            print("Maire : 'Merci, je savais que je pouvais compter sur vous.'")
            print("Maire : 'Des fées malintentionnées nous font chanter. Nous comptons sur vous pour nous aider. Elles habitent dans un étang situé non-loin de la ville.'")
            print("\nVous partez en direction de l'étang que le maire vous a indiqué.")
            print("Vous y trouvez les fées en train de barboter au bord de l'eau.")
            print("Les fées vous voient et comprennent aussitôt pourquoi vous êtes là. Il faut agir vite.")
            print("\n--- Que voulez-vous faire ? ---")
            print("1. Vous décidez d'utiliser la magie.")
            print("2. Vous décidez de passer en force.")
            print("3. Vous faites preuve d'ingéniosité.")
            print("4. Vous les brûlez violement pour leur assurer une mort rapide.")
            print("5. Vous les croquez pour mettre fin à leur règne tyrannique.")
            choix = input("Entrez le numéro de votre choix (entre 1 et 5) : ")

            if choix == '1':
                Dé = random.randint(1, 20)
                if Dé <= Magie:
                    print("Vous décidez d'utiliser la magie pour réussir.")
                    print("Les fées n'arrivent pas à vous contrer")
                    print("Vous réussissez à les vaincre.")
                else:
                    print("Vous tentez d'utiliser la magie.")
                    print("Vous échouez et vous battez en retraite.")
                    Dé = random.randint(1, 10)
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix == '2':
                Dé = random.randint(1, 20)
                if Dé <= Force:
                    print("Vous décidez de passer en force.")
                    print("Les fées n'ont pas le temps de réagir.")
                    print("Vous réussissez à les vaincre.")
                else: 
                    print("Vous tentez de passer en force.")
                    print("Vous échouez et vous battez en retraite.")
                    Dé = random.randint(1, 10)
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix == '3':
                Dé = random.randint(1, 20)
                if Dé <= Intelligence:
                    print("Vous faites preuve d'ingéniosité et vous faites en sortes que les fées s'embrouillent entre elles et s'entre-tuent.")
                    print("Vous réussissez à les vaincre.")
                else:
                    print("Vous tentez de faire preuve d'ingéniosité.")
                    print("Les fées sont trop intelligentes pour vous et votre ruse ne fonctionnent pas.")
                    Dé = random.randint(1, 10) 
                    Dégât = Dé
                    Vie -= Dégât
                    print(f"Vous avez perdu {Dégât} points de vie. Vous avez maintenant {Vie} points de vie.")
                    verifier_vie()
            elif choix == '4':
                if dragon is True:
                    print("Vous brûlez les fées qui disparaissent aussitôt.")
                    print("Vous les terrassez ainsi.")
                else:
                    print("Choix invalide. Veuillez sélectionner une option valide.")
                    sixieme_quete()
            elif choix == '5':
                if dragon is True:
                    print("Vous croquez les fées.")
                    print("Elles ne peuvent rien faire pour vous en empêcher.")
                    print("Vous réussissez à les vaincre.")
                else:
                    print("Choix invalide. Veuillez sélectionner une option valide.")
                    sixieme_quete()
            else:
                print("Choix invalide. Veuillez sélectionner une option valide. ")
                sixieme_quete()
    elif choix == '2':
            print("\nVous : 'Non monsieur j'estime que ce ne relève pas de mes obligations.'")
            tryndamere()
    else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.")
            sixieme_quete()
        
    print("\nFélicitations ! Vous avez réussi la quête 'Les Fées de l'étang'.")
    print("Vous avez débarassé la ville des fées qui ne subit plus le chantage.")
    print("Vous avez sauvé la ville de Tryndamere.")
    gain = random.randint(50, 100)
    print("Vous recevez une récompense de " + str(gain) + " pièces d'or.")
    Sixième_Quête = True
    argent += gain
    tryndamere()

# Fonction pour choisir la quête à Tryndamere
def tryndamere():
    global Troisième_Quête
    global Quatrième_Quête
    global Cinquième_Quête
    global emplacement_actuel
    emplacement_actuel = 'Tryndamere'
    if Quatrième_Quête is False:
        print("\nVous êtes dans la ville de Tryndamere. Vous avez une quête à faire :")
        print("---Que voulez-vous faire ?---")
        print("1. Commencer la quête 'Les Pillards de Tryndamere'.")
        print("2. Quitter la ville.")
        choix = input("Entrez le numéro de votre choix (1 ou 2) : ")
        if choix == '1':
            if Quatrième_Quête is False:
                quatrieme_quete()
            else:
                print("\nTu as déjà fait cette quête.")
                tryndamere()
        elif choix == '2':
            print("Vous quittez la ville de Tryndamere.")
            menu_principal()
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
            tryndamere()
        return "Tryndamere"
    elif Quatrième_Quête is True and Cinquième_Quête is False:
        print("\nVous êtes dans la ville de Tryndamere. Vous avez une quête à faire :")
        print("---Que voulez-vous faire ?---")
        print("1. Commencer la quête 'Les Pillards de Tryndamere'.")
        print("2. Commencer la quête 'Les Trolls du pont'.")
        print("3. Quitter la ville.")
        choix = input("Entrez le numéro de votre choix (Entre 1 et 3) : ")
        if choix == '1':
            if Quatrième_Quête is False:
                quatrieme_quete()
            else:
                print("\nTu as déjà fait cette quête.")
                tryndamere()
        elif choix == '2':
            if Quatrième_Quête is True and Cinquième_Quête is False:
                cinquieme_quete()
            elif Quatrième_Quête is False:
                print("\nChoix invalide. Veuillez sélectionner une option valide.")
                tryndamere()
            else:
                print("\nTu as déjà fait cette quête.")
        elif choix == '3':
            print("Vous quittez la ville de Tryndamere.")
            menu_principal()
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
            tryndamere()
        return "Tryndamere"
    elif Cinquième_Quête is True and Sixième_Quête is False:
        print("\nVous êtes dans la ville de Tryndamere. Vous avez trois quêtes à faire :")
        print("---Que voulez-vous faire ?---")
        print("1. Commencer la quête 'Les Pillards de Tryndamere'.")
        print("2. Commencer la quête 'Les Trolls du pont'.")
        print("3. Commencer la quête 'Les Fées de l'étang'.")
        print("4. Quitter la ville.")
        choix = input("Entrez le numéro de votre choix (Entre 1 et 3) : ")
        if choix == '1':
            if Quatrième_Quête is False:
                quatrieme_quete()
            else:
                print("\nTu as déjà fait cette quête.")
                tryndamere()
        elif choix == '2':
            if Quatrième_Quête is True and Cinquième_Quête is False:
                cinquieme_quete()
            elif Quatrième_Quête is False:
                print("\nChoix invalide. Veuillez sélectionner une option valide.")
                tryndamere()
            else:
                print("\nTu as déjà fait cette quête.")
        elif choix == '3':
            if Cinquième_Quête is True and Sixième_Quête is False:
                sixieme_quete()
        elif choix == '4':
            print("Vous quittez la ville de Tryndamere.")
            menu_principal()
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
            tryndamere()
        return "Tryndamere"
    else: 
        print("\nVous êtes à Tryndamere. Vous avez déjà fait toutes les quêtes disponibles ici.")
        print("Vous retournez à la croisée des chemins.")
        menu_principal()
        return "Tryndamere"

# Fonction pour la septième quête
def septieme_quete():
    global Septième_Quête
    Septième_Quête = False
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    print("\nCette quête n'est pas encore disponible.")
    print("Veuillez choisir une autre quête.")
    mordor()

# Fonction pour la huitième quête
def huitieme_quete():
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    print("\nCette quête n'est pas encore disponible.")
    print("Veuillez choisir une autre quête.")
    mordor()

# Fonction pour la neuvième quête
def neuvieme_quete():
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global argent
    global dragon
    print("\nCette quête n'est pas encore disponible.")
    print("Veuillez choisir une autre quête.")
    mordor()

# Fonction pour choisir sa quête à Mordor
def mordor():
    global emplacement_actuel
    emplacement_actuel = 'Mordor'
    global Septième_Quête
    global développeur
    if développeur is True:
        if Septième_Quête is False:
            print("\nVous êtes au village de Mordor. Vous avez une quête à faire.")
            print("---Que voulez-vous faire ?---")
            print("1. Commencer la quête 'Septième Quête'.")
            print("2. Quitter la ville.")
            choix = input("Entrez le numéro de votre choix (1 ou 2) : ")
            if choix == '1':
                if Septième_Quête is False:
                    septieme_quete()
                else:
                    print("\nTu as déjà fait cette quête.")
                    mordor()
            elif choix == '2':
                print("Vous quittez la ville de Tryndamere.")
                menu_principal()
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                mordor()
    else:
        print("Ce lieu n'est pas encore disponible.")
        print("Veuillez choisir un autre lieu.")
        menu_principal()

# Permet de répéter au joueur quel personnage il incarne. 
def personnage_incarné():
    global Vie
    global Force
    global Défense
    global Intelligence
    global Adresse
    global Magie
    global personnage
    global caractéristiques
    print(f"\nVous êtes un : {personnage}.")
    print(f"Caractéristiques : {caractéristiques}, Force : {Force}, Intelligence : {Intelligence}, Adresse : {Adresse}, Magie : {Magie}, Vie : {Vie}.")
    reprendre_jeu()

# Le jeu démarre ici grâce au renvoi de fonction
def début_du_jeu():
    global sauvegarde_chargee
    global nom_sauvegarde_chargée
    print("\n----Jeux de rôle interactif----\n")
    choix = input("Voulez vous charger une sauvegarde ? (oui/non) : ")
    if choix.lower() == 'oui':
        sauvegardes = lister_sauvegardes()
        if sauvegardes:
            print("Sauvegardes disponibles :")
            for i, nom in enumerate(sauvegardes):
                print(f"{i + 1}. {nom}")
            choix_sauvegarde = int(input("Entrez le numéro de la sauvegarde à charger : ")) - 1
            if 0 <= choix_sauvegarde < len(sauvegardes):
                sauvegarde_chargee = True
                nom_sauvegarde_chargée = sauvegardes[choix_sauvegarde]
                charger_jeu(sauvegardes[choix_sauvegarde])
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                début_du_jeu()
        else:
            print("Aucune sauvegarde disponible. Démarrage d'un nouveau jeu.")
            personnage, Force, Intelligence, Adresse, Magie, Vie, dragon = choisir_personnage()
            print("\nBonjour, bienvenue dans ce jeu de rôle interactif. Vous êtes un aventurier, et vous avez besoin de votre intelligence et de votre force.")
            print("Votre but seras d'accomplir différentes quêtes. Vous aurez des choix à faire, et vous devrez les choisir en fonction de votre personnage.")
            print("Vous aurez des pièces d'or en guise d'argent et vous devrez les utiliser pour acheter du matériel et des armes qui servirons à augmenter vos compétences.")
            sauvegarde_chargee = False
            menu_principal()
    elif choix.lower() == 'non':
        personnage, Force, Intelligence, Adresse, Magie, Vie, dragon = choisir_personnage()
        print("\nBonjour, bienvenue dans ce jeu de rôle interactif. Vous êtes un aventurier, et vous avez besoin de votre intelligence et de votre force.")
        print("Votre but seras d'accomplir différentes quêtes. Vous aurez des choix à faire, et vous devrez les choisir en fonction de votre personnage.")
        print("Vous aurez des pièces d'or en guise d'argent et vous devrez les utiliser pour acheter du matériel et des armes qui servirons à augmenter vos compétences.")
        sauvegarde_chargee = False
        menu_principal()
    else: 
        print("Choix invalide. Veuillez recommencer votre choix.")
        début_du_jeu()

# Ici démarre le programme après avoir tout défini. Renvoi à la fonction du début du jeu
début_du_jeu()