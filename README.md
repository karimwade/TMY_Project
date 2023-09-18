# TMY_Project
Projet test Lucisun
Projet realisé avec:
  - django python comme technologie backend
  - bootstrap pour le fronted(gerer la responsivité)
  - html - css - Javascript
creation de l'application tmy_app: avec python manage.py startapp app  tmy_app 
- modele pour déclarer la structure et le comportement attendus du TMY
- l'url pour définir les routes de l'application que  ce soit le formulaire de saisi du tmy ou le lien de telechargement du fichier yaml
- admin pour définir l'administration du systeme (on a mis en place un superutilisateur pour la gestion partie admin)
- views contenant toute la logique metier de l'application a savoir le create_tmy_parameter qui permet de sauvegarder les parametres dans la base de donées et de générer en plus le fichier yaml, on a aussi la vue success qui permet le telechargement du fichier yaml par un utilisateur
  on a installer le bibbliotheque yaml avec pip install pyyaml pour le traitement des fichier yaml
  on a utilisé db.sqlite3 comme base de données pour la gestion du backend
- Utilisation de mapbox et leaflet pour l'integration d'une carte pour la geolocalisation
    - creation d'un compte mapbox pour generer une clé afin de l'utiliser avec labiblioteque leaflet pour charger la carte 

