# sciMS
projet web implantant un CMS pour des article scientifiques

# outils utilises
plusieurs frameworks utilises:
* **django** : framework MVT cote serveur et utilisant le langage python
* **bootstrap** : framework css permettant l'adaptation aux tailles d'ecran

Plusieurs bibliotheques utilisees:
* **jquery** : bibliotheque javascript utilise avec bootstrap pour le design de l'application web
* **font-awesome**: bibliotheque d'icones

# Principe de Django

Django a ete developpe en 2003 par Adrian Holovaty et Simon Willison pour un journal local de Lawrence.

Ce framework a ete cree dans le but de pouvoir creer rapidement  des sites internets etant connectes a une base de donnees tout en suivant le principe du ***Don't repeat yourself*** (ne vous repetez pas) qui prone la factorisation du code.

Django est un framework suivant le principe MVT(model view template) cote serveur, c'est a dire que c'est le serveur qui construira les pages avant d'envoyer.

## MVT un MVC Particulier
Le framework django  respecte le principe du pattern MVT (Model View Template) qui suis lui meme le principe MVC (Model View Controller).<br/>
Cependant, le principe MVT est legerement different de MVT :
* Le *Model* du principe MVT est la base de donnee de l'application (en MVC, le **Model** est la partie communiquante avec la base de donnees)
* Le *View* du principe MVT est la partie recuperant les informations dans le modele et adaptant le template par rapport a ces informations ( c'est le **controller** dans le principe MVC)
* Le *Template* du principe MVT est l'ensemble des templates qui seronts retournes a l'utilisateur (c'est le **View** dans le principe MVC)

## le decoupage d'un application web avec django
Avec ce framework, nous decoupons l'application web en sous-applications, par exemple, un blog pourrait etre decoupe en 3 sous-applications :
* une application *index* etant la base de l'application web
* une application *article* etant l'application gerant les articles postes (la creation, la recuperation, la suppression,...)
* une application *chat* etant l'application gerant un chat en ligne (l'envoi de message, la reception de message,...)

Donc lorsque nous creons une application web, la premiere question a se poser est comment decouper son application.<br/>
Dans le projet sciMS, nous avons fait le choix de decouper l'application web  en 2 sous applications :
* *index* qui est la base de l'application (authentification, connexion, deconnexion, template de base de l'application web)
* *article* qui gere les articles (creation d'un article, creation d'une categorie, supression pour un article ou une categorie,...)

## les outils fournis par Django
Lorsque l'on utilise Django, tout n'est pas a faire soit meme, en effet, Django est un Framework, il nous fournit en plus du principe MVT certaines fonctionnalites deja crees.<br/>
Par exemple, nous pouvons utiliser le systeme d'authentification et de connexion deja fourni par django. Dans ce projet, nous n'avons que d'un systeme de base pour l'authentification,
nous avons donc utilises le systeme propose par Django.<br/>
Ce systeme fonctionne simplement, il suffit de creer un template avec un formulaire permettant de recuperer l'adresse mail et le mot de passe (fait en HTML) puis il faut creer une *route* permettant de lier ce template a la methode de login de la view de django.contrib.views

Il nous permet aussi de formater simplement des formulaires en python grace au module  django.forms<br/>
Grace a ce module, nous pouvons creer nos formulaires en pythons. L'avantage est que nous pouvons creer un formulaire et l'integrer dans plusieurs pages sans avoir a copier coller du code source, ce point est tres utile lorsque des modifications doivent etre effectuees dans le formulaire (il ne faut pas relire le projet en entier pour le changer a chaques endroits ou il est mis)

Django proposes d'autres paquets pour faciliter le developpement (cf doc officielle)

##Deploiment
 [RTFMN](https://docs.djangoproject.com/fr/1.10/howto/deployment/)

# contenu du projet
2 applications:
*  index : page principale du site (login, squelette de base)
*  article : page propre aux articles scientifiques

# utilisation de git sur ce projet
pour ajouter fichiers au git
*  aller a la racine du projet
*  utiliser git add .
*  utiliser git commit -m "MESSAGE PERTINENT"
*  utiliser git push
*  rentrer ton mot de passe

Pour changer de branche:
* utiliser git checkout [nom de la branche]

# liste des branches du projet
2 branches crees:
* master : branche principale ou le code est parfaitement fonctionnel (dans cette branche, le squelette fini pour le moment)
* article_view : branche secondaire servant pour le dev des article (modif des articles, creation des articles,...)

