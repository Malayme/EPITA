#!/bin/sh

#Script servant à lister tous les fichiers dans le répertoire courant

for FICHIER in $(ls); do
    echo "Fichier: $FICHIER"
done
