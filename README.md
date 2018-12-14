# GreenStarter
----------------
Projet Django GreenStarter sur des projets au profit de l'environnement, hébergé sur Apache2 en lien avec une base de données MariaDB.

# Installation
----------------
## Installation automatique via Docker :

Seul le fichier Dockerfile dans le dossier docker est nécessaire à la création de l'image Docker et du conteneur qui y sera lié.

Se placer dans le dossier docker et faire dans une console:
```
docker build . --tag="nom_image"
```
_Il est a noter que l'utilisation de `--tag` n'est pas obligatoire mais fortement conseillé pour gérer facilement vos images._

Pour créer le conteneur
```
docker run -d -p 8000:80 --name="nom_conteneur" nom_image
```
_Même remarque que plus haut pour `--name`._

Ici, `-d` exécute le conteneur en tâche de fond et `-p` map un port du système hôte (8000) au port de sortie du conteneur (80).
Donc vous pouvez accéder au site à l'adresse suivante: `localhost:8000`

## Installation manuel
### Dépendances requises
**Programmes**
* Python 3.5
* apache2
* mysql-server
* libapache2-mod-wsgi-py3

**Modules Python :**
* django == 1.11 (LTS)
* mysqlclient == 1.3.13
* pytz == 2018.7
* django-material == 1.4

Vous pouvez automatiser leurs installations grâce à pip3 et au fichier requirements à la racine du projet :
```
pip3 install -r requirements.txt
```

### Mise en place
Remplacez la configuration d'Apache2 dans /etc/apache2 par apache2.conf dans le dossier docker, puis redémarrez le service.
Placez le projet dans /var/www/html, placer vous dedans et lancez dans une console :
```
python3 manage.py collectstatic --noinput
```

### MariaDB
Concernant la base de données, la configuration de Django se trouve dans greenstarter/settings.py.  
Nous vous conseillons **très** fortement de changer les informations de connexions à la base de données !  
**La base de données et l'utilisateur doivent déjà exister avant de passer à l'étape suivante !**

Pour mettre en place la structure de la base de données dans MariaDB, exécutez dans une console :
```
python3 manage.py makemigrations && python3 manage.py migrate
```

C'est fini ! GreenStarter est en place et servie sur le port 80 de votre machine, sauf si vous avez changé la configuration d'Apache2 bien sûr !


Lui il va faire le build, run, il va voir localhost:8000 et terminé. si ça marche pas c'est 0.

Donc il faut faire des tests.

Compte rendu:
* Site fonctionnel note >10
* fonctionnalité et lien logique note 15/16
* le reste de la note c'est le docker
