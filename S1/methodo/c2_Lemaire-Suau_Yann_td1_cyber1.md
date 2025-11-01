# Instructions

- Vous devez rédiger les réponses dans ce fichier, en respectant le format Markdown, après l'avoir téléchargé à partir de ce lien. Vous pouvez le télécharger à partir de ce [lien](https://gitlab.com/mpuren/methodo-travail-cyber1/-/raw/main/cours1_demarrer_projet_gitlab/fiche_td1_cyber1.md?ref_type=heads).
- Pour ces exercices, **vous devez travailler en ligne de commande**. Copiez les commandes exécutées dans votre terminal et formatez-les correctement en Markdown. Pour vous aiderr à formater votre fichier en Markdown, consultez "[Les outils de travail](https://gitlab.com/mpuren/methodo-travail-cyber1/-/blob/main/cours1_demarrer_projet_gitlab/4.%20Les%20outils%20de%20travail.md?ref_type=heads)".
- Lorsque que cela vous sera demandé, vous **ajouterez des captures d'écran**.
- La fiche de travaux dirigés (TD) terminée doit être disponible sur GitLab, correctement formatée. Les captures d'écran devront s'afficher sans problèmes lorsque l'on consulte le document dans votre dépot.
- La fiche d'exercice doit être nommée en suivant cette convention : `groupe_nom_prénom_td1_cyber1.md`. Remplacez `groupe` par le numéro de votre groupe en minuscules (a1, a2, b1, b2, c1, c2, d1, d2).
- Une fois que vous avez terminé,
  - supprimez ces instructions,
  - poussez cette fiche en markdow, renommée comme demandé, dans le dépôt distant que vous avez créé durant les premiers exercices.

> Durant les 2 derniers exercices, vous devrez ajouter Mme Puren (`@mpuren`) en tant que membre de votre projet, de façon à ce qu'elle puisse lire et commenter votre rendu. Vous créerez une issue ou ticket pour lui assigner la tâche de corriger vos exercices.

**Si ces instructions ne sont pas respectées, le TD sera considéré comme non rendu.**

> **UN CONSEIL AVANT DE COMMENCER** : 
> - Avant de débuter un exercice, lisez le entier et réfléchissez quelques instant à ce que vous allez faire.
> - Vous pouvez prendre des notes avant de débutez les exercices : c'est toujours utile quand on n'est pas sûr(e) de soi ou quand on veut vérifier que l'on suit le bon raisonnement. :-)

# Création d'un dépôt distant

*Pour vous aiderr, vous pouvez utilisez les documents dans le répertoire "[Prérequis](https://gitlab.com/mpuren/methodo-travail-cyber1/-/tree/main/cours0_prerequis?ref_type=heads)" et "[Démarrer un projet GitLab](https://gitlab.com/mpuren/methodo-travail-cyber1/-/blob/main/cours1_demarrer_projet_gitlab/4.%20D%C3%A9buter%20un%20projet%20avec%20GitLab.md?ref_type=heads)".*

## Exercice 1 : Vérifier la configuration de son Git - 0,5 point
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Comment afficher les configurations de votre Git ?
```bash
  git config --list
```


- Comment savoir quel est l'utilisateur et l'email configurés ?
```bash
git config user.name
git config user.email
```


- Comment savoir quel est l'éditeur configuré ?

```bash
git config core.editor
```

- Après avoir exécuté ces commandes, copiez les résultats obtenus.

*git config --list*
```bash
credential.helper=osxkeychain
user.name=Yann LS
user.email=yannls.cbv@gmail.com
color.diff=auto
color.status=auto
color.branch=auto
core.editor=vim
merge.tool=vimdiff
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
user.name=Yann LS
(END)
```

*git config user.name*
```bash
➜  methodo git:(master) ✗ git config --global user.name                     
YannLS
```

*git config user.email*
```bash
➜  methodo git:(master) ✗ git config user.email
yannls.cbv@gmail.com
```
*git config core.editor*

```bash
➜  methodo git:(master) ✗ git config core.editor                       
vim
```
- Comment configurer le nom de l'utilisateur, l'email et l'éditeur ?

```bash
git config --global user.name "Nom"
```
```bash
git config --global user.email "email"
```

```bash
git config --global core.editor "éditeur"
```
- En fonction des résultats obtenus dans la partie 1, configurez le nom de l'utilisateur, l'email et l'éditeur en copiant les commandes utilisées et les résultats. Si vous ne pensez pas devoir le faire, justifiez.

Je ne modifie pas mes mon nom d'utilisateur et mon email car j'utilise git et github depuis un certain temps et que tout modifier changerai toute mon organisation et je recevrai plus d'email pour la double authentification par exemple. Et pour Vim, j'ai éffectué la piscine de 42 et donc des Exam Machines semblables à ceux d'EPITA donc j'y suis déjà habitué.

## Exercice 2 : Créer un projet sur GitLab - 2 points
*Vous utiliserez des captures d'écran pour présenter vos résultats.*

Vous allez créer un projet sur GitLab qui vous permettra de rendre vos exercices.

- Créez un projet vide (sans `README.md`) sur GitLab. 

![Erreur](/Users/yannls/Documents/EPITA/methodo/travail-1-methodo/Capture.png)

  - Expliquez pourquoi il vaut mieux créer un projet vide.

Il vaut mieux créer un projet vide sans même de README car ça nous permet d'avoir un meilleur contrôle et organisation sur notre projet.

  - Expliquez comment vous avez procédé.
  - Vous êtes libre de nommer le projet comme vous le souhaitez. Toutefois, vous devez respecter une convention de nommage. Expliquez comment vous avez nommé votre projet.
- Allez dans les paramètres de votre projet et vérifiez les paramètres. Expliquez et justifiez la visibilité que vous avez choisie.

**Exercice avancé** : Expliquez pourquoi bien choisir la visibilité est importante. Donnez un exemple de situation où chaque type de visibilité serait approprié.

### Exercice 3 : Créer un fichier `.gitignore` - 0,5 point
*Vous utiliserez des captures d'écran pour présenter vos résultats.*

- Expliquez, avec vos propres mots, à quoi sert un fichier `.gitignore`.
- Créez un fichier `.gitignore` depuis l'interface GitLab. Expliquez comment vous avez procédé et faite une capture d'écran du fichier obtenu.

## Exercice 4 : Ajouter une licence - 0,5 point
*Vous utiliserez des captures d'écran pour présenter vos résultats.*

- Créez un nouveau fichier [licence](https://gitlab.com/mpuren/methodo-travail-cyber1/-/blob/main/cours1_demarrer_projet_gitlab/4.%20D%C3%A9buter%20un%20projet%20avec%20GitLab.md?ref_type=heads#choisir-une-licence) pour votre projet depuis l'interface GitLab.
- Choisissez une licence parmi les options proposées, par exemple :  MIT, GPL, ou Creative Commons

**Exercice avancé** : 
Expliquez l'importance de choisir la bonne licence pour un projet. Comparez deux types de licences, par exemple **MIT** et **Creative Commons**, et discutez des avantages et des inconvénients de chacune.

## Exercice 5 : Cloner le dépôt GitLab sur sa machine locale - 2 points
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Où avez-vous décidé de cloner votre dossier sur votre ordinateur ? Copiez le chemin d'accès.
- Clonez le projet GitLab sur une machine locale et indiquez comment vous avez procédé. Pensez à copier les commandes utilisées et les résultats obtenus dans votre terminal
- Vérifiez que le projet a bien été cloné en listant les fichiers dans le répertoire du projet. Expliquez comment vous procédez.

# Révision des principales commandes

*Pour vous aiderr, vous pouvez utilisez les documents dans le répertoire[Prérequis](https://gitlab.com/mpuren/methodo-travail-cyber1/-/tree/main/cours0_prerequis?ref_type=heads).*

## Exercice 6 : Ajouter des modifications à l'index - 2 points
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Créez un fichier appelé `README.md`.
- Modifiez le fichier en ajoutant du texte : par exemple, indiquez la licence que vous avez choisie d'utiliser.
- Expliquez ce qu'est l'index dans Git, et à quoi il sert.
- Maintenant, ajoutez `README.md` à l'index, mais sans valider le commit.
- Vérifiez l'état de votre projet.

**Exercice avancé 1** :
- Modifiez à nouveau `README.md` en ajoutant deux sections différentes de texte (par exemple, ajoutez un titre de niveau 1 et un titre de 2) et une phrase expliquant pourquoi vous avez créé ce projet.
- Quelle commande utilisez-vous pour n'ajouter que certaines parties des modifications ?
- Exécutez cette commande et expliquez quelles étapes vous devez suivre pour sélectionner les changements spécifiques à inclure. Par exemple, choississez de n'inclure que votre texte explicatif.

**Exercice avancé 2** :
- Finalement, vous ne souhaitez pas ajouter votre fichier modifié à l'index. Que faîtes-vous ?
- Suuprimez le fichier de l'index.
- Vérifiez le statut de votre projet.

## Exercice 7 : Pousser un fichier sur un dépôt distant - 2 points
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Quelle commande faut-il utiliser pour valider l'ajout du README  ?
- Que se passe t-il une fois que vous avez validé cet ajout ?
- Exécutez les commandes pour valider votre ajout. Pensez à expliciter la raison de cet ajout.
- Poussez ce fichier vers GitLab et copiez la commande que vous avez exécutée.
- Faîtes une capture d'écran pour montrer que le fichier a bien été ajouté et apparaît dans l'interface GitLab.

## Exercice 8 : Modifier le message de commit - 1 point
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Modifiez le fichier `README.md` en ajoutant des détails supplémentaires : par exemple, indiquez à quel groupe vous appartenez. 
- Modifiez le message du dernier commit avant de pousser les modifications.
- Affichez le message de commit sur l'interface Gitlab et faîtes une capture d'écran.
- Expliquez pourquoi cette commande peut être utile et comment elle affecte l'historique du projet.

## Exercice 9 : Mettre à jour un projet GitLab localement - 2 points
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Modifiez le `README.md` directement dans l'interface GitLab : par exemple, indiquez que vous allez rendre en tout quatre fiches de TD.
- Synchronisez les modifications sur votre machine.
- Vérifiez que les changements sont bien récupérés dans votre dépôt local.

**Exercice avancé** : Expliquez en quoi la commande `git fetch` diffère de celle que vous venez d'utiliser et dans quelles situations il est préférable de l'utiliser.

## Exercice 10 : Visualiser les logs et réinitialiser un commit - 2 points
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Créez un fichier `nom_prenom.txt` et ajouter à la première ligne votre Nom, Prénom.
- Ajoutez-le à votre projet.
- Créer un fichier `template_cr_reunion.md` et ajoutez dans le document la phrase (sans les guillemets) : "Ceci est un modèle pour un compte-rendu de réunion."
- Ajoutez-le à votre projet.
- Affichez l'historique de votre projet.
- Utilisez une des options offertes par la commande que vous venez d'utiliser pour obtenir un affichage plus compact.

## Exercice 11 : Annuler un commmit - 1 point
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Quelle commande faut-il utiliser pour annuler le dernier commit sans affecter l'index ?
- Indiquez l'identifiant de votre avant dernier commit. Comment le trouvez-vous ?
- Annulez ce commit, sans affecter l'historique.

## Exercice 12 : Comparer les modifications - 2 points
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Modifiez le `README`, `nom_prenom.txt` et `template_cr_reunion.md`, en ajoutant les phrases suivantes :
  - Dans le 1er fichier : Lorem ipsum dolor sit amet, consectetur adipiscing elit.
  - Dans le 2ème fichier : César, Jules
  - Dans le 3ème fichier : Nullam ultrices dictum sapien at tempus.
- Quelle commande pouvez-vous utiliser pour comparer les modifications non validées avec la version la plus récente dans votre répertoire de travail ?
- Expliquez le résultats obtenus.
- Ajoutez `nom_prenom.txt` à l'index. Quelle commande vous permet de comparer ajoutées à l'index mais non encore committées ?

## Exercice 13 : Travailler avec les fichiers supprimés - 1 point
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Supprimez le fichier `nom_prenom.txt` avec la commande `rm`.
- Quelle commande pouvez-vous utilisez pour voir comment Git affiche cette suppression.
- Comment pouvez-vous indiquer cette suppression à Git ?
- Supprimez également ce fichier dans votre projet GitLab et montrez le résultat avec une capture d'écran.

# Les messages de commit

## Exercice 14 : La structure d’un bon message de commit - 1 point
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Modifiez le `README` en ajoutant un commentaire : `<!-- Ceci est un fichier readme écrit en Markdown --->`
- Utilisez la commande appropriée pour ajouter un commentaire détaillé avec votre éditeur. Copier la commande utilisée et faîtes une capture d'écran de votre éditeur ouvert. 
- Rédigez un message structuré avec :
     - **Une ligne de titre** (moins de 50 caractères) décrivant brièvement la modification.
     - **Un corps de message** (au moins 2 lignes) expliquant pourquoi cette modification a été effectuée.
- Validez le commit après avoir rédigé le message.

**Exercice avancé** : Expliquez pourquoi il est important d'avoir une ligne de titre courte et d'ajouter une description détaillée pour certains commits. Comment cela aider-t-il à la gestion des projets complexes ?

## Exercice 15 : Utilisation de messages de commit multiples sans éditeur - 1 point
*Vous illustrerez vos réponses en copiant les commandes utilisées. Vous copierez également les résultats obtenus après avoir exécuté les commandes.*

- Modifiez le fichier `nom_prenom.txt` en ajoutant votre email avec votre nom et prénom.
- Ecrivez cette fois un commit détaillé sans ouvrir votre éditeur. Comment procédez-vous ?

# Créer des issues sur GitLab
Pour vous aiderr, vous pouvez consulter "[Créer et gérer des issues avec GitLab](https://gitlab.com/mpuren/methodo-travail-cyber1/-/blob/main/cours1_demarrer_projet_gitlab/5.%20Cr%C3%A9er%20et%20g%C3%A9rer%20des%20issues%20avec%20GitLab.md?ref_type=heads)".

## Exercice 16 : Créer une issue sur GitLab - 1 point
*Vous utiliserez des captures d'écran pour montrer comment vous avez procédez.*

- Créez une issue avec Gitlab. Elle doit s'intituler "Correction du TD 1.
- Ajoutez une description plus détaillée, en expliquant que vous créez cette issue dans le but de permettre à Mme Puren de corriger et noter votre TD.

## Exercice 17 : Assigner des issues à des utilisateurs - 0,5 point
*Vous utiliserez des captures d'écran pour montrer comment vous avez procédez.*

- Ajoutez Mme Puren comme membre de votre dépôt. Choisissez son statut de façon à ce qu'elle puisse visualiser les issues, les commenter et les fermer.
- Justifiez le choix de ce statut.
- Assigner l'issue à Mme Puren.