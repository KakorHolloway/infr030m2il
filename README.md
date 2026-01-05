# infr030-m1rs

## Connection au cluster Openshift
Pour vous connecter au cluster Openshift mis à disposition :

### Pour trouver les sources rendez-vous dans la release suivante : https://github.com/okd-project/okd/releases/tag/4.19.0-okd-scos.19

### Pour Windows x86

Téléchargez sur votre machine le paquet OKD suivant : 
https://github.com/okd-project/okd/releases/download/4.19.0-okd-scos.19/openshift-client-windows-4.19.0-okd-scos.19.zip

Copiez le fichier oc.exe dans C:\Windows\System32

### Pour Linux x86
Téléchargez sur votre machine le paquet OKD suivant : 
https://github.com/okd-project/okd/releases/download/4.19.0-okd-scos.19/openshift-client-linux-4.19.0-okd-scos.19.tar.gz

Dézippez et copiez le fichier oc dans /urs/bin
```
tar -xvf openshift-client-linux-4.19.0-okd-scos.19.tar.gz
cp oc /usr/bin/
```

### Pour MAC

Télécharger le client suivant 

https://github.com/okd-project/okd/releases/download/4.19.0-okd-scos.19/openshift-install-mac-arm64-4.19.0-okd-scos.19.tar.gz pour ARM

https://github.com/okd-project/okd/releases/download/4.19.0-okd-scos.19/openshift-install-mac-4.19.0-okd-scos.19.tar.gz pour x86

Mettez le fichier oc dans le path.

Ou alors :
```
brew install openshift-cli
```


## Connexion au cluster (pour tous)

Allez sur l'url https://console-openshift-console.apps.openshift.kakor.ovh authentifiez-vous avec l'utilisateur ipi-gp-x (le x étant le numéro de groupe) en choisisant "KeystoneIDP".

Une fois authentifié (attention à ne pas recharger la page même si l'affichage prends du temps), allez en haut à droite de la page et sélectionnez l'option "Copy login Command" et réauthentifiez vous. 

Cliquez sur le lien Display Token et copiez dans votre terminal sur VScode la ligne de commande qui à été donné avec oc. 

Pour vérifier que vous êtes authentifiés, lancez la commande ```oc get pod```

## Exo 1) Création de votre premier pod

Via un fichier yaml ou une commande impérative ( oc run <monpod>... ), créez votre premier pod httpd. 

Celui-ci doit utiliser l'image suivante: harbor.kakor.ovh/public/httpd:latest

Afin de confirmer que le pod existe, utilisez la commande ```oc get pod```

``` oc logs <nomduconteneur> ``` => permet d'identifier les logs du conteneur et ainsi trouver des réponses à des problèmes techniques. 

### Pour corriger le crashloopbackoff en cas de problème de compte root

Dans le fichier yaml :

```
apiVersion: v1
kind: Pod
metadata:
  name: httpd
spec:
  containers:
  - name: httpd
    image: harbor.kakor.ovh/public/httpd:latest
    securityContext:
      allowPrivilegeEscalation: true
    ports:
    - containerPort: 80
```

Autre option : refaire l'image (ou utiliser une autre image) pour que celle-ci ne nécéssite pas l'utilisation de l'utilisateur root, par exemple on peut utiliser cette image :

harbor.kakor.ovh/public/nginx-rootless:latest

### Exo 1.1) Supprimez le pod existant pour mettre à jour avec la nouvelle image.  


### Comment vérifier que le conteneur fonctionne bien ? 

On peut : 

- Vérifier le status sur Kubernetes (Est-il en Running ?)
- Tester dans le conteneur des commandes :
   ``` oc exec -it <nomconteneur> -- /bin/bash``` ou ```oc exec -it <nomconteneur> -- /bin/sh ```

## Exo 2 ) Création d'un service avant l'ingress

- Supprimez les pods de votre namespace

- Créez le pod suivant avec le label de votre choix:

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    <aremplir>
spec:
  containers:
  - image: harbor.kakor.ovh/public/nginx
    name: nginx
    securityContext:
      allowPrivilegeEscalation: true
```

- Créez le service suivant et modifiez le pour qu'il se connecte au pod:

```
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  selector:
    <a remplir>
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

Si tout marche bien, créez l'ingress suivant et testez si vous accédez au site :

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx
spec:
  rules:
    - host: <nomdevotresite>.apps.openshift.kakor.ovh
      http:
        paths:
        - path: ''
          pathType: ImplementationSpecific
          backend:
            service:
              name: nginx
              port:
                number: 80
  tls:
  - {}
```

## Exo 3) Limits et Requests

A partir du deployment de l'exercice 3 : 

- Tentez de déployer un pod sans mettre de limit ou request et supprimez-le (vérifiez les limits qui sont positionnées (en théorie vous ne devriez rien voir))
- Mettez en place un LimitRange avec 0,25 cpu et 0,5 Gb de RAM 
- Tentez à nouveau de déployer le pod
- Mettez à jour le deployment pour mettre 100m CPU (0,1 vCPU) et 50 Gb de RAM => Voyez ce qu’il se passe, dans quel état sont les pods ? 
- Supprimez le limitRange
- Mettez des valeurs de limits semblable au LimitRange 

## Exo4

Nettoyez les actions de l'exercice 3 (limitrange et deployment)

- Créez un deployment avec 5 pods qui va faire en sorte que les pods soient tous dans des noeuds différents (https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity)
- Vérifiez qu'un des pods ne se déploie pas 
- Faites en sorte que si ils peuvent les pods seront dans des noeuds différents et sinon ils pourront quand même se déployer. 

## Exo 5 Les configmaps

- Créez une page web simple en html.
- A partir de cette page créez une configmap (le fichier html dans la configmap devra avoir le nom index.html)
- A partir du fichier deployment.yaml dans le dossier exo5, montez le fichier index.html récupéré de la configmap précédemment créée. 
- Vérifiez depuis votre navigateur le bon fonctionnement de votre montage. 

Pour vous aider voici la documentation des configmaps :

https://kubernetes.io/docs/concepts/configuration/configmap/


## Exo 6 : Les secrets

- Créez un conteneurs mysql à partir de l'image : harbor.kakor.ovh/public/mariadb:latest
- Ce conteneur devra avoir une variable d'environnement lui permettant de définir le mot de passe root (cf mariadb sur Docker Hub)
- Mettez ce mot de passe dans un secret