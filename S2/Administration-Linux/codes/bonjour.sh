######################################################################################################################
# This simple script ask to the user his name with the command read. Then, it verify if the value is gratter than 18 #
######################################################################################################################

#!/bin/sh

echo "Quel est votre nom ?"
read NOM

echo "Bonjour, $NOM"

echo "Quel est votre âge ?"
read AGE

if [ $AGE -gt 18 ]; then
    echo "Vous êtes majeur."
else
    echo "Vous êtes mineur."
fi
