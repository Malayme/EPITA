#!/bin/sh

FILENAME="default"
NUMBER=1
EXTENSION="txt"

while [ "$#" -gt 0 ]; do
    if [ "$1" = "-f" ] || [ "$1" = "--filename" ]; then
        FILENAME="$2"
        shift 2
    elif [ "$1" = "-n" ] || [ "$1" = "--number" ]; then
        NUMBER="$2"
        shift 2
    elif [ "$1" = "-e" ] || [ "$1" = "--extension" ]; then
        EXTENSION="$2"
        shift 2
    else
        echo "CA MARCHE PAS $1"
        exit 1
    fi
done

for i in $(seq 1 "$NUMBER"); do
    touch -- ${FILENAME}-${i}.${EXTENSION}
done

exit 0


