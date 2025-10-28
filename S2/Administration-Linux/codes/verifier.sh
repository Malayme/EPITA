#!/bin/sh


if [ -e "test.txt" ]; then

    for FICHIER in $(ls); do
        echo "Fichier: $FICHIER"
    done

else
    echo "Le fichier n'existe  pas."
fi