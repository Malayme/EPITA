
Install IDA

1- DL fichiers sur moodle
2- creer archive : cat ida.part* > ida.tgz
				tar xf ida.tgz
3- Install : ./ida
4- Copier Licence 
5- ./ida crackme ===> export PATH=$PATH:/chemin/install

## Strategie Statique

Chaines de caracteres 
fonctions exportees
fonctions importees
Selon la surface :
- reverser un protocole reseau
- reverser un lanceur de programme
- reversesr un algo

Graph d'appel = representation de tous les appels des fonctions

Control Flow Graph (CFG) = Representation de l'ensemble des chemins possibles d'exec d'un programme, le flux d'execution

Basic Block = Noeud du CFG, contient des intructions toutes executees ensembles, sa sortie modifie le control flow

DFG = Data Flow Graph

## Reverse Dynamique

Methodo :
- code strippe / compile en statique / contient des symboles de debug ?
- code obfusque ?
On peut savoir alors : 
- valeurs parametres fonctions 
- flux reel d'execution et de donnees

Strategie protocole : 
- Isole API qui manipulent le protocole
- Isole les fonctions qui lisent et ecrivent par ce protocole
- Inspecter la memoire
- Coder un parseur (language au choix)

### Outils :

- peda / gef/ pwntools (wrapper sur gdb)
- windbg
- radare2
- IDA (mod debuggeur)
- ollydbg / x64dbg (windows)

GDB : 

2 types de breakpoints : 
- software = programme qui implemente
- hardware = processeur qui implemente

