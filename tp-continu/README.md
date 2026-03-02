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
````docker run -d -p 5000:5000 monimage:latest ````

## Exercice 2) Mettez votre image sur harbor

Connectez vous sur harbor.kakor.ovh avec docker :

``` docker login harbor.kakor.ovh ```

L'utilisateur c'est ipi 

Mot de passe B4teau123!

Changez le nom de votre image pour la pousser sur harbor comme suit:

```docker tag monimage:latest harbor.kakor.ovh/ipi/votrenom:latest ````
``` docker push harbor.kakor.ovh/ipi/votrenom:latest ```

Vérifiez les vulnérabilités de votre image.

## Exercice 3) 

à travers l'aide de l'exercice 2 du cours original, déployez votre application sur internet à travers le cluster Kubernetes 

Pour rappel l'utilisateur c'est ipi-gp-x et le mot de passe habituel. 