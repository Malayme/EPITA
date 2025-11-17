
Concepts - annuaire LDAP/Active Directory
Deployer et gerer un domaine AD dans environnement  Windows Server
reseau d'entreprise, postes de travail au domaine
Creer utilisateurs, groupes, OU (unite d'organisation) configurer delegations
Mettre en place archi multi domaine, controleurs de domaine et relation d'approbations
Deployer strategies de groupe (GPO), scripts partage reseau SMB
Comprendre fonctionnement authentification Kerberos

## Eval : 
Premiere moitie:
- CM avec quizz
- TP non note
Deuxieme moitie :
- Projet en groupe binome
- Real reseau multi-domaine, acces par pont sur Wi-Fi EPITA ou point acces mobile
- Rapport a rendre, documenter etape

------------------
AD -> Annuaire LDAP dev par Microsoft : gestion centralisee et securisee 
Annuaire: BDD pour stocker et infos sur users, ordinateurs et ressources

LDAP Lightweight Directory Access Protocol: Interroge et modif sur TCP/IP. Respect modele X500

Objet = ID unique
DN = distinguished name, permet de trouver un objet
cn=Toto,ou=Cyber,dc=epita,dc=local

CN = Common Name
OU = Organizational Unit
DC = Domain Component

Differents types d'objets :
- user
- ordis
- serveurs
- OU
- groupes
Objet=Classe, memes attributs

OU = container d'autres objets, permissions, facilite l'orga

3 partitions de repertoire = Naming Context
- Partition de Domaine
- Partition de schema
- Partition de configuration

AD DS (Active Directory Domain Service)

Service = 1 user (compte de service)

computers = Security Principals
MDP machines = rotation automatique de 120 caracteres aleatoirs
compte machine est suivi d'un $ a la fin
Groupe de Securite = Possed un SID (numero qui permet a un groupe de s'identifier), Security Principals
Groupe = User + Com, peut inclure d'autre groupe

-------------------------------
## TP 1 - Installation

