#!/bin/sh

echo "Entrez un mot à rechercher"
read MOT
grep -i "$MOT" /etc/passwd