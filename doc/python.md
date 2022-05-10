# Python

###### tags `Cours` 

* Version
    * `py -V`
    * `py -3 --version`

# :gift: Packages 

### pip

* programme pour installer des packages
* https://phoenixnap.com/kb/install-pip-windows

### Autopep8

* Pour bien mettre en forme le code
* Possibilité dans Visual Studio code d'executer autopep8 à chaque sauvegarde de fichier

```bash
C:\Ludo>py -m pip install autopep8     # installer
cd P:/...mon_dossier.../
python -m autopep8 -i my_file.py       # executer
```



### Numpy 

```bash
C:\Ludo>py -m pip install numpy     # installer
```

* https://courspython.com/apprendre-numpy.html

### Doc diverse

* Méthodes statiques : https://pythonforge.com/methodes-de-classes-et-statiques/


---



# :crystal_ball: Visual Studio Code 

* https://code.visualstudio.com/docs/python/python-tutorial
* Utilisation : https://code.visualstudio.com/docs/languages/python

### :gear: Settings

* pour formatter le code à chaque sauvegarde de fichier
    * python.formatting.autopep8
    * editor.formatOnSave :heavy_check_mark:


---

# :open_file_folder: Git - paramètrage

* [Git by Donatien](https://donatien26.gitlab.io/website/ensai/projet1A_2021/index.html#/)


### 1. Config Git bash

:::info
Git permet de faciliter la synchronisation du code entre : 
* notre poste : dépôt local (ou personnel)
* GitHub : dépôt distant (ou commun)
:::

Ouvrir git bash et entrer les commandes suivantes (la dernière permet de vérifier)
```bash=
git config --global user.name "Ludovic Deneuville"
git config --global user.email ludovic.deneuville@eleve.ensai.fr
git config -l
```


### 2. Clé SSH

toujours dans Git bash, lancer cette commande et taper ENTREE à chaque question

```bash=
ssh-keygen -t rsa -b 4096 -C "ludovic.deneuville@eleve.ensai.fr"
cat /p/.ssh/id_rsa.pub
```

* La commande cat renvoi tout le contenu de ce fichier.
* Sélectionner ce contenu pour le copier et le garder de côté pour la prochaine étape


### 3. Créer un compte sur GitHub


:::info
GitHub est le site qui permet d'héberger le dépôt distant du code
:::

* https://github.com/
* Aller dans **Settings** (en haut à droite) puis dans **SSH and GPG keys**
    * ou directement ici : https://github.com/settings/keys
* Cliquer sur **New SSH key**
    * title : ma_cle_ensai (en fait mettez ce que vous voulez)
    * key : coller le résultat de l'étape 2
    * Add SSH Key

### 4. Cloner le code

:::spoiler
Si le projet n'est pas déjà créé dans GitHub, aller sur son profil > Repositories > New
:::

* Créer le dossier suivant **P:\projet-info-sources**
* Dans Git Bash, taper
```bash=
cd P:/projet-info-sources
git clone git@github.com:ludo2ne/Projet-info.git
```

* Are you sure... :arrow_right: taper **yes**
* Et voila le code du projet est importé dans le dossier **P:\projet-info-sources** qui est votre dépôt local

---


# :open_file_folder: Git - utilisation

### 1. Avant de commencer à coder

* Ouvrir **Git Bash**
```bash=
cd P:/projet-info-sources/Projet-info
git pull
```

le **git pull** permet d'importer en local toutes les modifications qui auraient pu être faite par les autres depuis la dernière fois

### 2. Je code

* je crée/modifie/supprime des fichiers python
* je teste que ça fonctionne bien
* une fois que j'ai fait un bon morceau qui fonctionne, je crée un commit (point de sauvegarde)

```bash=
git add .                 # permet d'ajouter tous les nouveaux fichiers créés
git status                # pour voir les changements en cours (c'est la commande que l'on utilise le plus)
git commit -am "message explicite"        # Pour creer un commit
```
* Si par la suite je fais une connerie, c'est facile de revenir au commit précédent
:::spoiler
* :warning: cette commande supprime toutes les modifications depuis le dernier commit
    * :bulb: par sécurité, copier/coller le dossier **Projet-info** avant de lancer la commande
```bash=
git reset --hard
```
:::

### 3. Je partage mon oeuvre

* Si les autres n'ont rien foutu entre temps, tout va bien :+1: 
* Par contre si l'un d'eux a modifié le dépôt distant, il faut d'abord synchroniser ton dépôt local avec les modifications effectuées par cet enfoiré avant de partager ton code
* Si vous n'avez pas touché aux mêmes fichiers
    * c'est cool ça va bien se passer :+1: 
* Si vous avez touché au même fichier, c'est là que ça devient drole :face_palm: 
    * :rotating_light: CONFLICT (content): Merge conflict - Automatic merge failed :rotating_light: 
    * il faut ouvrir le fichier en conflit et on voit apparaitre ceci 
```
<<<<<<< HEAD
"Les modifs que j'ai faites"
=======
"Les modifs faites par l'autre con"
>>>>>>>
```
* il ne reste plus qu'à modifier le fichier pour choisir quelle modif on garde
    * puis restester que tout est ok
    * puis recréer un commit `git commit -am "merge manuel a cause de lautre con"`
    * et enfin faire son `git push`


```bash=
git pull           # pour recuperer les eventuelles modifs du depot distant
git status         # pour voir s il n y a pas de conflits
git push           # pousser son code vers depot distant
```

### Commandes - ce qu'il faut retenir

```bash=
git status               # Voir ce qui est en cours
git pull                 # Copier depot distant vers depot local
git push                 # Copier depot local vers depot distant

git add .                # Avant un commit pour que git identifie les nouveaux fichiers
git commit -am "message" # Creer un point de sauvegarde
```
