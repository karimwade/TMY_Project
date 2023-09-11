# TMY_Project
Projet test Lucisun
Projet réalisé avec django python comme framework backend et bootstrap pour le front et gerer en meme temps la responsivité
Utilisation de  db.sqlite3 comme base de donnée pour le backend en creant un super utilisateur pour les interactions admin
creation de l'application tmy_app ou on renseigne 
.le model 
.les urls(home pour le formulaire de saisie et success pour la redirection du fichier yaml créer)
.views qui contient toute la logique métier de l'application à savoir la fonction create_tmy_parameter qui permet de recuperer les parametres du TMY de le sauvegarder dans la base de données et de généré un fichier yaml qui par suit va etre telechargeable depuis l'url telecharger fichier yaml (géré par la vue success)
