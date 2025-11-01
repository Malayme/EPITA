#!/bin/sh

if [ $# -ne  1 ]; then
    exit 1
fi


if [ $1 -lt 0 ]; then
    exit 1
fi

nbr=$1
fact=1

while [ $nbr -gt 1 ]; do
    fact=$((fact * nbr))
    nbr=$((nbr - 1))
done

echo $fact

exit 0

