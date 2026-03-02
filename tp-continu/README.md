# Demonstration DevOps

Lien aide : 

https://devopssec.fr/article/creer-ses-propres-images-docker-dockerfile#begin-article-section

## Exercice 1) Mise en place de l'image docker pour votre applicatif

Créez l'image docker permettant de lancer l'application python flask contenue dans le dossier app.

Pour créer votre docker file, partez de l'image python officielle

Intallez les dépensenses flask (pip)

Copiez votre applicatif 

Exposez le port 5000

Lancer l'application avec l'entrypoint permettant d'exécuter l'applicatif. 

Si possible ajouter un utilisateur sans uid spécique pour s'exécuter sur Openshift

Testez en local une fois le build fait que votre conteneur fonctionne correctement. 

Attention votre fichier doit obligatoirement se nommer Dockerfile

````docker build -t monimage:latest .````
````docker run -d monimage:latest ````