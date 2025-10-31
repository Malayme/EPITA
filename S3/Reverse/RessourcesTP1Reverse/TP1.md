## Exercice 1

### En utilisant les outils gcc et objdump, trouver comment refaire l’exemple du cours pour l’architecture x86-64 linux.
Commandes : 
gcc -S hello-world.c
gcc  hello-world.c -o hello-world.o
objdump --disassemble (--reloc) -M intel hello-world.o
hexdump -C hello-world.o


### Comment faire pour les autres architectures ? Qu’est-ce que c’est que la compilation croisée ?
Il faut installer un compilateur croise.
La **compilation croisée** consiste à compiler un programme sur une machine (hôte) pour qu’il s’exécute sur une autre machine (cible) avec une architecture différente.
Commande :  
arch64-linux-gnu-gcc
arch64-linux-gnu-objdump
### Expliquer le concept de code natif et code managé.
Le code natif est compile directement en assembly pour une architecture dite. Tandis que le manage est compile dans un autre language pour pouvoir etre compile sur une autre machine.

## Exercice 2

Télécharger les binaires et observer leurs structures avec les outils objdump / file :
Exécuter la commande :
File <binaire> puis interprétez le résultat pour tous les binaires.
Exécuter la commande :
file bin1
bin1: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=766cd676d07b53d7e6a7e098095e59ce3b169d70, for GNU/Linux 3.2.0, not stripped
file bin2.exe
bin2.exe: PE32+ executable (console) x86-64, for MS Windows, 18 sections
file bin3
bin3: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.3, BuildID[sha1]=56f9cf7bb0e7c716c25d270983229ddd34b366a8, for GNU/Linux 3.2.0, not stripped
file bin7
bin7: ELF 64-bit LSB pie executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, BuildID[sha1]=7649e8b466da206d858a91afb37a7ce86636a86a, for GNU/Linux 3.7.0, not stripped

Objdump –d –M intel <binaire> en remplaçant <binaire> par les différents exécutables. Que peut-on
observer sur les registres et l’ABI utilisée ?
Plus de section sur Windows. Section en commun .text .data

Exécuter la commande :
Objdump –h <binaire> en remplaçant binaire par les différents exécutables. Utiliser le manuel pour
savoir ce que fait la commande. Interprétez.


## Exercice 3

Télécharger le squelette ex3.asm à partir de moodle. Nous allons utiliser les outils jwasm / gcc /
objdump dans cet exercice.
Compiler le fichier avec les commandes suivantes :
-
-
Jwasm –elf64 ex3.asm && gcc –nostdlib ex3.o
Objdump –d –M intel a.out
Expliquer ce que font les instructions push / pop / mov rax, [rsp+10] / cmp et noter leurs opcodes.

push : **Fonction** : Empile une valeur sur le sommet de la pile (stack). **Effet** : Décrémente `rsp` (pointeur de pile) de 8 octets (pour x86-64), puis stocke la valeur à l’adresse pointée par `rsp`. 
Opcode : 50 et 53

pop : ## `pop`

**Fonction** : Dépile une valeur du sommet de la pile. **Effet** : Lit la valeur à l’adresse pointée par `rsp`, puis incrémente `rsp` de 8 octets. 
Opcode : 59 et 5a

## `mov rax, [rsp+10]`

**Fonction** : Charge une valeur depuis la mémoire à une adresse calculée, dans un registre. **Explication** :

- `rsp` pointe sur le sommet de la pile.
- `[rsp+10]` signifie : "lis la valeur à l’adresse `rsp + 10`".
- La valeur lue est stockée dans `rax`.
Opcode : 48 c7 44 24 10 37 13 et 

Expliquer les sauts conditionnels ja / jne / je / jg
Quel est l’opcode généré pour un jg ? et pour un ja ?
Expliquer la ligne :
104d: eb 00
jmp 104f <_start+0x4f>Que se passe t’il si on remplace le eb 00 par eb fe ? Expliquer.

`je`Jump ======== if Equal ============== ZF = 1

`jne` =========== Jump if Not Equal ====== ZF = 0

`ja` ============ Jump if Above (>) ====== CF = 0 **et** ZF = 0 (non signé)

`jg` =========== Jump if Greater (>) ===== ZF = 0 **et** SF = OF (signé)

`jb` =========== Jump if Below (<) ====== CF = 1 (non signé)

`jl` =========== Jump if Less (<) ======== SF ≠ OF (signé)

En remplaçant `eb 00` par `eb fe`, on transforme ce saut neutre en une **boucle infinie**.

##  Exercice 4

Faire l’exemple du cours slide 45 en utilisant gcc. Expliquer
Ecrire un petit programme pour mettre en évidence la taille des types int / long / pointeur sous linux
et windows.

Mettre par exemple int i = sizeoff(long);
La taille sera ecrite apres : mov QWORD PTR [rbp-0x4], TAILLE

## Exercice 5: crackme du cours avec objdump, première approche vers RE statique
Observer avec objdump et bvi (pour modifier le binaire) le fonctionnement du programme et
répondez aux questions suivantes :
Quelles sont les pistes qu’on peut suivre pour comprendre le fonctionnement de ce
programme ?
Observer le fonctionnement des sauts conditionnels
Observer les appels aux sous-fonctions et expliquer le passage de paramètre
Investiguez pour trouver quels sont les paramètres de la fonction strncmp juste en regardant
l’assembleur.
Modifier les sauts conditionnels pour valider le crackme
Retrouver le mot de passe recherché sans exécuter le binaire.

Le code vient de la derniere slide du cours

