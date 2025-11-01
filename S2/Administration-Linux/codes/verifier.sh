#!/bin/sh

# Scrip permettant de vérifier si un fichier existe dans le répertoire courant

if [ -e "test.txt" ]; then

    for FICHIER in $(ls); do
        echo "Fichier: $FICHIER"
    done

else
    echo "Le fichier n'existe  pas."
fi
