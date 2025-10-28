#!/bin/sh

#affiche le nom compet de l'hôte complet
hostname -f

echo "#####"

#afficher uniquement les lig,es de lscpu qui commencent par "CPU"
lscpu | grep "^CPU"

echo "#####"

#Afficher le contenu de /etc/selinux/config en en ignorant les lignes vides et les commentaires
grep -v -E '^$|^#' /etc/selinux/config

echo "#####"

#Afficher toutes les entrées "Mounted " dans /var/log/boot.log 

grep "Mounted " /var/log/boot.log 

echo "#####"

# Vérifier si un utilisateur spécifique existe 
UTILISATEUR="root"

if id "$UTILISATEUR" > /dev/null 2>&1; then
    echo "L'utilisateur $UTILISATEUR existe."
    echo "Information sur l'utilisateur:"

    id "$UTILISATEUR"

else

    echo "L'utilisateur $UTILISATEUR n'existe pas."

fi

echo "#####"

# Afficher la mémoire disponible avec free (en Mo)

echo "Mémoire disponible:"

free -m | grep "Mem:"


