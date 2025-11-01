#!/bin/sh

# Script permettant de rechercher un mot suivant un chemin spécifique

echo "Entrez un mot à rechercher"
read MOT
grep -i "$MOT" /etc/passwd
